import os

import gradio as gr

from modules import paths, script_callbacks, shared

from scripts.eagleapi.item.addFromPath import add_from_path

DEBUG = False
def dprint(str):
    if DEBUG:
        print(str)

path_root = paths.script_path

def on_ui_settings():
    # flg: Enable/Disable
    shared.opts.add_option("enable_eagle_integration", shared.OptionInfo(False, "Send all image to Eagle", section=("eagle_pnginfo", "Eagle Pnginfo")))
    # specify Eagle folderID
    shared.opts.add_option("save_to_eagle_folderid", shared.OptionInfo("", "FolderID on Eagle (option)", component_args=shared.hide_dirs, section=("eagle_pnginfo", "Eagle Pnginfo")))
    # flg: save generation info to annotation
    shared.opts.add_option("save_generationinfo_to_eagle_as_annotation", shared.OptionInfo(False, "Save Generation info as Annotation", section=("eagle_pnginfo", "Eagle Pnginfo")))
    # flg: save positive prompt to tags
    shared.opts.add_option("save_positive_prompt_to_eagle_as_tags", shared.OptionInfo(False, "Save positive prompt to Eagle as tags", section=("eagle_pnginfo", "Eagle Pnginfo")))
    shared.opts.add_option("save_negative_prompt_to_eagle_as", shared.OptionInfo("n:tag", "Save negative prompt as", gr.Radio, {"choices": ["None", "tag", "n:tag"]}, section=("eagle_pnginfo", "Eagle Pnginfo")))

# image saved callback
def on_image_saved(params:script_callbacks.ImageSaveParams):
    if not shared.opts.enable_eagle_integration:
        dprint(f"DEBUG:on_image_saved:  DISABLED")
    else:
        dprint(f"DEBUG:on_image_saved:  ENABELD. enable_eagle_pnginfo is true.")
        # collect info
        fullfn = os.path.join(path_root, params.filename)
        info = params.pnginfo.get('parameters', None)
        filename = os.path.splitext(os.path.basename(fullfn))[0]
        #
        pos_prompt = params.p.prompt
        neg_prompt = params.p.negative_prompt
        #
        annotation = None
        tags = []
        if shared.opts.save_generationinfo_to_eagle_as_annotation:
            annotation = info
        if shared.opts.save_positive_prompt_to_eagle_as_tags:
            if len(pos_prompt.split(",")) > 0:
                tags += [ x.strip() for x in pos_prompt.split(",") if x.strip() != "" ]
        if shared.opts.save_negative_prompt_to_eagle_as == "tag":
            if len(neg_prompt.split(",")) > 0:
                tags += [ x.strip() for x in neg_prompt.split(",") if x.strip() != "" ]
        elif shared.opts.save_negative_prompt_to_eagle_as == "n:tag":
            if len(neg_prompt.split(",")) > 0:
                tags += [ f"n:{x.strip()}" for x in neg_prompt.split(",") if x.strip() != "" ]
        # send to Eagle
        _ret = add_from_path(filefullpath=fullfn, filename=filename, annotation=annotation, tags=tags, folderId=shared.opts.save_to_eagle_folderid)
        dprint(_ret)
        dprint(f"content    :{_ret.content}")
        dprint(f"status_code:{_ret.status_code}")

# on_image_saved
script_callbacks.on_image_saved(on_image_saved)

#
script_callbacks.on_ui_settings(on_ui_settings)
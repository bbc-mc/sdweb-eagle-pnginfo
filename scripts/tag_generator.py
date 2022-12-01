from modules import shared


class TagGenerator():
    # @seealso modules.images FilenameGenerator replacements
    # @seealso modules.processing create_infotext generation_params
    replacements ={
        "Steps": lambda self: self.p.steps,
        "Sampler": lambda self: self.p.sampler_name,
        "CFG scale": lambda self: self.p.cfg_scale,
        "Seed": lambda self: self.p.seed if self.p.seed is not None else '',
        "Face restoration": lambda self: (shared.opts.face_restoration_model if self.p.restore_faces else None),
        "Size": lambda self: f"{self.p.width}x{self.p.height}",
        "Model hash": lambda self: getattr(self.p, 'sd_model_hash', None if not shared.opts.add_model_hash_to_info or not shared.sd_model.sd_model_hash else shared.sd_model.sd_model_hash),
        "Model": lambda self: (None if not shared.opts.add_model_name_to_info or not shared.sd_model.sd_checkpoint_info.model_name else shared.sd_model.sd_checkpoint_info.model_name.replace(',', '').replace(':', '')),
        "Hypernet": lambda self: (None if shared.loaded_hypernetwork is None else shared.loaded_hypernetwork.name),
        "Hypernet strength": lambda self: (None if shared.loaded_hypernetwork is None or shared.opts.sd_hypernetwork_strength >= 1 else shared.opts.sd_hypernetwork_strength),
        "Variation seed": lambda self: (None if self.p.subseed_strength == 0 else self.p.seed),
        "Variation seed strength": lambda self: (None if self.p.subseed_strength == 0 else self.p.subseed_strength),
        "Seed resize from": lambda self: (None if self.p.seed_resize_from_w == 0 or self.p.seed_resize_from_h == 0 else f"{self.p.seed_resize_from_w}x{self.p.seed_resize_from_h}"),
        "Denoising strength": lambda self: getattr(self.p, 'denoising_strength', None),
        "Conditional mask weight": lambda self: getattr(self.p, "inpainting_mask_weight", shared.opts.inpainting_mask_weight) if self.p.is_using_inpainting_conditioning else None,
        "Eta": lambda self: (None if self.p.sampler is None or self.p.sampler.eta == self.p.sampler.default_eta else self.p.sampler.eta),
        "Clip skip": lambda self: None if getattr(self.p, 'clip_skip', shared.opts.CLIP_stop_at_last_layers) <= 1 else getattr(self.p, 'clip_skip', shared.opts.CLIP_stop_at_last_layers),
        "ENSD": lambda self: None if shared.opts.eta_noise_seed_delta == 0 else shared.opts.eta_noise_seed_delta
        }

    def __init__(self, p=None, image=None):
        self.p = p
        self.image = image

    def generate_from_geninfo(self, tags_to_eagle, geninfo):
        geninfo = geninfo.split("\n")
        if len(geninfo) == 3:
            geninfo = geninfo[2]
        else:
            return []
        # generate lists from geninfo. i.e) "Steps: 30, CFG scale: 7.5" -> ["Steps: 30", "CFG scale: 7.5"]
        geninfo_params = [ x.strip() for x in geninfo.split(",") if x.strip() != "" ]
        geninfo_dict = {}  # {"Steps": "30", "CFG scale": "7.5"}
        for item in geninfo_params:
            geninfo_dict.update({item.split(":")[0]: item.split(":")[1].strip()})
        tag_list = [ x.strip() for x in tags_to_eagle.split(",") if x.strip() != "" ]
        _tags = [ f"{x}: {geninfo_dict.get(x)}" for x in geninfo_dict.keys() if x in tag_list ]
        return _tags

    def generate_from_p(self, tags_to_eagle):
        tag_list = [ x.strip() for x in tags_to_eagle.split(",") if x.strip() != "" ]

        tags = []
        for _tag in tag_list:
            if not _tag or _tag == "":
                continue
            func = self.replacements.get(_tag)
            if func:
                try:
                    _tag_data = func(self)
                except Exception as e:
                    print(e)
                    _tag_data = ""
                if _tag_data:
                    tags += [f"{_tag}: {_tag_data}"]
        tags = [ x for x in tags if x.strip() != "" ]
        return tags

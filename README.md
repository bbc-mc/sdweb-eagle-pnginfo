# Eagle-pnginfo

![](misc/sss_top.png)

[日本語 README はこちら](README.ja.md)

- This is Extension for [AUTOMATIC1111's Stable Diffusion Web UI](https://github.com/AUTOMATIC1111/stable-diffusion-webui)
- Send your creation image to [Eagle](https://jp.eagle.cool/) (image management software) with Generation info, tags.

## How to Install

- Go to `Extensions` tab on your web UI

- `Install from URL` with this repo URL

- Install

- Install [Eagle]([https://jp.eagle.cool/](https://jp.eagle.cool/))

## How to use

- Enable this extension in "Setting"

- Start "Eagle" application

- Open "AUTO1111" and create image as usual.
  
   - images sent to "Eagle" automatically

## About Setting params

| In "Setting" tab                        | ![](misc/sss08.png)                                                                                                                                              |
| --------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| "Send all image to Eagle"               | Enable this extension                                                                                                                                            |
| "FolderID on Eagle (option)"            | (option) Specify folder by ID on Eagle to input images                                                                                                           |
| "Save Generation info as Annotation"    | Save PNGinfo style text to "memo" on Eagle                                                                                                                       |
| "Save positive prompt to Eagle as tags" | Save each prompt word as tag on Eagle                                                                                                                            |
| "Save negative prompt to Eagle as"      | Save each negative prompt word as tag on Eagle<br/>None  : disabled<br/>tag   : normal tag. i.e.) "bad anatomy"<br/>n:tag : tag with "n:". i.e.)"n:bad annatomy" |

## Setting sample

| Settings              | Result                | Comment                                                                                                            |
| --------------------- | --------------------- | ------------------------------------------------------------------------------------------------------------------ |
| ![](misc/sss00.png)   | No output to Eagle    |                                                                                                                    |
| ![](misc/sss01-1.png) | ![](misc/sss01-2.png) | Image sent to Eagle, only with filename.                                                                           |
| ![](misc/sss02-1.png) | ![](misc/sss02-2.png) | Image sent to Eagle with Generation info.                                                                          |
| ![](misc/sss03-1.png) | ![](misc/sss03-2.png) | Image sent to Eagle, with Generation info, tags from positive prompt                                               |
| ![](misc/sss04-1.png) | ![](misc/sss04-2.png) | Image sent to Eagle, with Generation info, tags from negative prompt                                               |
| ![](misc/sss05-1.png) | ![](misc/sss05-2.png) | Image sent to Eagle, with Generation info, tags from negative prompt decorated with "n:".<br/> i.e.) n:bad anatomy |
| ![](misc/sss06-1.png) | ![](misc/sss06-2.png) | Image sent to Eagle, with Generation info, tags from positive prompt and negative prompt decorated with "n:".      |
| ![](misc/sss07-1.png) | FolderID              | You can get "Eagle forlderID" on Eagle UI. Right click folder and select "copy link".                              |
| ![](misc/sss07-4.png) | ![](misc/sss07-3.png) | Input folderID.                                                                                                    |
| ![](misc/sss07-2.png) |                       | Bad sample of folderID.<br/>Only right-end value required.                                                         |

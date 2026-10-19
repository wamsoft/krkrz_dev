---
source_hash: 7daa58891598
---

# Movie Playback

This page describes the movie playback features supported by Kirikiri Z.

### Contents

[Specifications](#spec)

[Modes](#mode)

[Supported formats and decoders](#codec)

[How overlay compositing works](#overlay_compose)

[Movie playback on SDL (GENERIC)](#generic)

[Trick play features](#trickplay)

[Preparing movie playback (preparevideo)](#preparevideo)

[Specifying layers in layer mode](#layermode)

[Behavior at the end of a movie](#end_of_video)

[Movies not appearing in layer mode](#layer_alpha)

[Mixing playback](#mixer_mode)

[Keyframes and seeking](#seek_to_keyframe)

## Specifications { #spec }

| &nbsp; | &nbsp; | &nbsp; |
| --- | --- | --- |
| Mode | Overlay mode (vomOverlay) | Uses a video overlay to display the movie in front of everything (full screen) |
| Mode | Layer mode (vomLayer) | Decodes and plays the movie into a specified layer |
| Mode | Mixer mode (vomMixer) | Displays the movie with additional layer images composited on it (always software compositing) |
| Trick play | Segment loop | Loops between specified frames |
| Trick play | Period event | Fires an event at a specified frame |
| Trick play | Playback rate | Specifies the movie's playback rate |
| Trick play | Multi-audio | Selects and plays one of multiple multiplexed audio streams |
| Audio balance<br>(panning) | -100000 to 0<br>to 100000 | -100000 is fully left, 0 is center, 100000 is fully right.<br>When playing a stereo source, panning is achieved<br>by attenuating either the left or right channel. |
| Audio volume | 0 to 100000 | 0 is fully muted, 100000 is 100% volume |
| Audio stream | Depends on content | Selects the audio stream to play |
| Playback rate | > 0 | 1.0 is normal speed. With audio, the upper limit is roughly 2.0 ≥ rate > 0. |
| Retrievable values | Frame rate | Frames per second |
| Retrievable values | Current frame | The frame currently displayed.<br>Not guaranteed to match the displayed frame number exactly. |
| Retrievable values | Current playback time | Elapsed time within the movie from its beginning. |
| Retrievable values | Image size | Width and height |
| Retrievable values | Number of audio streams | Number of multiplexed audio streams |
| Retrievable values | Total frames | Number of frames the movie contains |
| Retrievable values | Total time | Total duration of the movie |
| Event | Frame update | Fires after a video frame is updated |
| Event | Period event | Fires at the end of a normal loop, at the end of a segment loop,<br>at a configured period event, and when playback preparation completes. |
| Event | Status change | Fires when the playback state changes |

`VideoOverlay.visible` is a property that controls only whether the movie is displayed; its default is false. Decoding and audio playback proceed regardless of `visible` (behavior inherited from Kirikiri 2/Z). You can use this to prepare or prefetch without displaying anything, or to advance only the audio.

## Modes { #mode }

| Type | Description |
| --- | --- |
| Overlay mode (vomOverlay) | The default mode, which displays the movie in front of everything (full screen). It appears in front of all other layers.<br>On WINVER, the video is composited into the Direct3D 11 back buffer of the draw device (BasicDrawDevice).<br>Best suited for simply playing and stopping a movie, and it has the lowest load. It does not composite additional images (use mixer mode if you need that).<br>For compatibility, the constant vomMFEVR remains as an alias of vomOverlay. |
| Layer mode (vomLayer) | Decodes and plays the movie into a specified layer.<br>It depends little on the environment and supports features such as looping between specified frames (segment loop) and processing at specified frames (period events).<br>Its drawback is higher CPU load than the other modes. |
| Mixer mode (vomMixer) | In addition to the overlay, this mode can composite a layer image specified with `setMixingLayer` on top of the movie.<br>To reliably composite the additional image, this use case never uses hardware decoding and always takes the software compositing path. |

## Supported formats and decoders { #codec }

On WINVER, the following decoders are used depending on the file extension and container.

| Format | Decoder | Notes |
| --- | --- | --- |
| webm (VP8 / VP9) | movie-player | Supports webm with an alpha channel. |
| mpg / mpeg (MPEG-1) | pl_mpeg | Supports multiplexed audio streams (multi-audio). |
| wmv / asf / mp4 / mov / avi, etc. | Media Foundation SourceReader | Decodes to BGRA on the CPU (CPU path). |
| mp4 / wmv, etc. (MF native) | IMFMediaEngine (HW decoding) | Hardware-decoded by default. Specifying `-mediaengine=no` disables it and falls back to the CPU SourceReader. |

The IMFMediaEngine HW decoding path shares BasicDrawDevice's Direct3D 11 device. Audio playback and AV synchronization are handled internally by MediaEngine.

## How overlay compositing works { #overlay_compose }

Overlay (and mixer) video is passed to the draw device through a pull-type VideoPresenter. BasicDrawDevice's `Show` requests a frame from the presenter every frame and composites it into the back buffer.

When the active draw device has no host that accepts a presenter, playback falls back to Direct3D 11 present using a child window.

`System.captureScreen` captures the screen by reading back the back buffer, so the capture includes the overlay video.

## Movie playback on SDL (GENERIC) { #generic }

On the SDL (GENERIC) builds, webm is decoded with movie-player and MPEG-1 with pl_mpeg.

There are SDL_Renderer and OpenGL versions of the video presenter; the OpenGL version performs BT.601 YUV→RGB conversion in a shader. Emscripten (web) uses the browser's `<video>`.

For overlay / mixer playback (vomOverlay / vomMixer), the playback rectangle (`setPos` / `setSize` / `setBounds`) works the same as in the Windows build. While none of these are specified, the movie is displayed over the whole screen with its aspect ratio preserved; once specified, it is displayed in that rectangle on top of the game screen. The browser build (Emscripten) behaves the same way.

Movie audio is played through miniaudio (MovieAudioSink). The number of samples played is used as the master clock for AV synchronization, and the video follows it.

## Trick play features { #trickplay }

| Type | Description |
| --- | --- |
| Segment loop | Loops between specified frames.<br>To use this feature, the movie file itself must have a keyframe at the frame the loop jumps back to.<br>Without a keyframe, the loop will not work as expected. |
| Period event | Fires an event at a specified frame so that you can perform some processing.<br>By seeking to a distant frame when the event fires, you can skip the frames in between and make the movie appear continuous.<br>It can also be used to show subtitles in sync with a movie: set a period event at the subtitle's start frame and display the text when the event arrives.<br>You can also leave the movie itself silent and play sound effects at specified frames. |
| Playback rate control | The movie's playback rate can be specified.<br>1.0 is normal speed, 0.5 is half speed, and 2 is double speed.<br>The configurable range depends on the decoder / codec. |
| Multi-audio | Takes advantage of MPEG-1's ability to multiplex multiple audio streams.<br>This feature lets you play any of the audio streams.<br>For example, you can prepare streams such as BGM only and BGM + voice, and let the user choose which one to play.<br>However, switching audio streams has a lag of about 2 seconds, so it is not well suited to highly interactive uses.<br>It works for cases like the user selection above, or when the movie audio changes depending on the scene. |

## Preparing movie playback (preparevideo) { #preparevideo }

preparevideo draws the first frame of the movie into the specified layer.

It is used to prevent unintended images (garbage in memory, a previous image, etc.) from appearing on screen.

In other words, by hiding the target layer, opening the movie with openvideo, calling preparevideo, waiting for preparation to complete, and then making the target layer visible, the first frame of the movie is shown as soon as the layer appears.

Note that this feature is meaningful only in layer mode.

## Specifying layers in layer mode { #layermode }

When playing a movie in layer mode, use videolayer to specify the target layer.

videolayer accepts slot, channel, page and layer.

slot identifies which video an operation applies to when different videos are played at the same time.

Playing multiple movies simultaneously is rare, so normally you can omit it and let 0 be used.

channel specifies the output layer.

Up to two output layers can be specified per movie, and channel identifies which of the two the specification applies to.

Two are allowed so that transitions can be used.

Running a transition during movie playback swaps the fore and back layers, so if output goes to only one of them, the movie disappears.

To avoid this, when you run a transition during movie playback, set the fore and back layers to channels 1 and 2. If you do not use transitions, specifying only the fore layer is enough.

## Behavior at the end of a movie { #end_of_video }

When a movie is played without looping, it stops after playing to the end.

This is undesirable if you want the game to proceed while the last frame of the movie stays on screen.

The simplest way to avoid this is to use layer mode.

In layer mode, the movie is drawn into a layer, so the image of the last frame remains in the layer.

The game can therefore proceed with the last frame displayed, without any special handling.

With overlay or mixer, the display disappears when playback stops, so you must pause before reaching the last frame.

This can be done with a period event, but pausing exactly at the last frame may result in the movie stopping, so it is better to add a few dummy frames at the end of the movie so that slightly overshooting is harmless.

## Movies not appearing in layer mode { #layer_alpha }

If the display type of the target layer is alpha or similar, the movie may not appear.

This is because, when the movie has no alpha channel, undefined data is written into the alpha channel position.

When the layer display type is alpha, this undefined data is treated as alpha values, which can make the layer completely transparent.

To avoid this, set the target layer's display type to opaque.

The movie will then be displayed.

## Mixing playback { #mixer_mode }

As its name suggests, mixer mode plays the movie mixed with other layers.

In mixer mode, the settings related to mixing are the background color, the blend ratio and the mixing target layer.

The mixing target layer's image at the moment it is set is mixed with the movie.

Therefore, even if the mixing target layer is updated, its content is not updated unless it is set again.

However, calling the setter on every frame update makes CPU load considerably high.

To keep CPU load down, set it only when the layer has actually been updated.

The background color is the color blended in when the blend ratio is less than 1.0.

By setting the background color to black or similar and changing the blend ratio, you can achieve fade-in / fade-out.

Naturally, fade-in / fade-out with the mixing target layer is also possible.

The blend ratio and position for the mixing target layer are taken from the layer's own information.

That is, the display position depends on the layer's position, and the blend ratio depends on the layer's opacity.

However, because blending with the layer must be specified each time, fading in / out with a layer increases CPU load.

## Keyframes and seeking { #seek_to_keyframe }

To make seeking fast, Kirikiri Z limits seekable positions to keyframes.

When a frame other than a keyframe is specified, the seek goes to the keyframe closest to the specified frame.

However, this behavior depends on the codec, so it often behaves unexpectedly.

It is therefore best to always place a keyframe at any frame you seek to.

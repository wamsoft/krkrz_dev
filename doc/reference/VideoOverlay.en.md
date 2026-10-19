# VideoOverlay

The VideoOverlay class creates a display area for showing movies. It can also display on Kirikiri layers.

The movie playback mechanism (krmovie) is integrated into the engine executable, so no separate DLL needs to be shipped.
Playback does not use DirectShow: WebM is decoded with movie-player (libvpx), MPEG-1 with pl_mpeg, and everything else (WMV/ASF/MP4 and so on) with
Media Foundation. Formats native to Media Foundation, such as MP4/WMV, are hardware-decoded by default
(this can be disabled with the command-line option -mediaengine=no). The former theora support (krdstheora.dll) is not available.

Except for playback on a layer, with overlay playback the display area of the VideoOverlay class is shown in front of all layers and cannot be transparent.

Playback on a layer tends to put a higher load on the processor than overlay playback.

The SDL build and other non-native-Windows builds can play WebM and MPEG-1.

**How playback ends (playback on a layer)**: the last frame is shown for the same duration as any other frame (one frame's worth of time)
before playback ends (`"stop"` in onStatusChanged) or rewinds for a loop (`perLoop` in onPeriod).
The last frame stays on the layer after playback ends. When making a looping animation, you do not need to
append a copy of the first picture at the end to make the seam (if you do, the first picture lasts for two frames).

## Members

### Constructors

- [VideoOverlay](#videooverlay)

### Properties

- [position](#position)
- [frame](#frame)
- [loop](#loop)
- [width](#width)
- [height](#height)
- [left](#left)
- [top](#top)
- [visible](#visible)
- [fps](#fps)
- [numberOfFrame](#numberofframe)
- [totalTime](#totaltime)
- [layer1](#layer1)
- [layer2](#layer2)
- [mode](#mode)
- [playRate](#playrate)
- [segmentLoopStartFrame](#segmentloopstartframe)
- [segmentLoopEndFrame](#segmentloopendframe)
- [periodEventFrame](#periodeventframe)
- [audioBalance](#audiobalance)
- [audioVolume](#audiovolume)
- [numberOfAudioStream](#numberofaudiostream)
- [enabledAudioStream](#enabledaudiostream)
- [mixingMovieAlpha](#mixingmoviealpha)
- [mixingMovieBGColor](#mixingmoviebgcolor)
- [contrastRangeMin](#contrastrangemin)
- [contrastRangeMax](#contrastrangemax)
- [contrastDefaultValue](#contrastdefaultvalue)
- [contrastStepSize](#contraststepsize)
- [contrast](#contrast)
- [brightnessRangeMin](#brightnessrangemin)
- [brightnessRangeMax](#brightnessrangemax)
- [brightnessDefaultValue](#brightnessdefaultvalue)
- [brightnessStepSize](#brightnessstepsize)
- [brightness](#brightness)
- [hueRangeMin](#huerangemin)
- [hueRangeMax](#huerangemax)
- [hueDefaultValue](#huedefaultvalue)
- [hueStepSize](#huestepsize)
- [hue](#hue)
- [saturationRangeMin](#saturationrangemin)
- [saturationRangeMax](#saturationrangemax)
- [saturationDefaultValue](#saturationdefaultvalue)
- [saturationStepSize](#saturationstepsize)
- [saturation](#saturation)
- [originalWidth](#originalwidth)
- [originalHeight](#originalheight)
- [enabledVideoStream](#enabledvideostream)
- [numberOfVideoStream](#numberofvideostream)

### Methods

- [open](#open)
- [play](#play)
- [stop](#stop)
- [pause](#pause)
- [rewind](#rewind)
- [prepare](#prepare)
- [setSegmentLoop](#setsegmentloop)
- [cancelSegmentLoop](#cancelsegmentloop)
- [close](#close)
- [setPeriodEvent](#setperiodevent)
- [cancelPeriodEvent](#cancelperiodevent)
- [setPos](#setpos)
- [setSize](#setsize)
- [setBounds](#setbounds)
- [selectAudioStream](#selectaudiostream)
- [setMixingLayer](#setmixinglayer)
- [resetMixingLayer](#resetmixinglayer)

### Events

- [onStatusChanged](#onstatuschanged)
- [onPeriod](#onperiod)
- [onFrameUpdate](#onframeupdate)
- [onCallbackCommand](#oncallbackcommand)

---

### VideoOverlay

Constructor

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `window` | `&nbsp;` | The window (an object of the [Window](Window.md) class) that will own this<br>layer. |

**Description**

Constructs a VideoOverlay object

Constructs an object of the VideoOverlay class.

---

### position

Property \ Access: `r/w`

**Description**

Playback position

The playback position of the media in ms. You can also set this value.

The position of the first frame is 0.

**See also:** [VideoOverlay.frame](VideoOverlay.md#frame) / [VideoOverlay.totalTime](VideoOverlay.md#totaltime)

---

### frame

Property \ Access: `r/w`

**Description**

Current frame

The playback position of the media in frames. You can also set this value.

The first frame is 0.

**See also:** [VideoOverlay.position](VideoOverlay.md#position) / [VideoOverlay.numberOfFrame](VideoOverlay.md#numberofframe)

---

### loop

Property \ Access: `r/w`

**Description**

Whether to loop playback

Indicates whether loop playback is enabled. You can also set this value.

True loops; false does not.

In loop playback, the last frame is shown for one frame before returning to the beginning, and onPeriod (`perLoop`)
occurs. While looping, `"stop"` in onStatusChanged does not occur. This also works in the SDL build and others.

---

### width

Property \ Access: `r/w`

**Description**

Width of the playback rectangle

The width of the playback rectangle. You can also set this value.

In the current version, this property cannot be used during layer playback (the size is always the same as the video size).

**See also:** [VideoOverlay.height](VideoOverlay.md#height) / [VideoOverlay.setSize](VideoOverlay.md#setsize)

---

### height

Property \ Access: `r/w`

**Description**

Height of the playback rectangle

The height of the playback rectangle. You can also set this value.

In the current version, this property cannot be used during layer playback (the size is always the same as the video size).

**See also:** [VideoOverlay.width](VideoOverlay.md#width) / [VideoOverlay.setSize](VideoOverlay.md#setsize)

---

### left

Property \ Access: `r/w`

**Description**

Left edge of the playback rectangle

The left edge of the playback rectangle. You can also set this value.

**See also:** [VideoOverlay.top](VideoOverlay.md#top) / [VideoOverlay.setPos](VideoOverlay.md#setpos)

---

### top

Property \ Access: `r/w`

**Description**

Top edge of the playback rectangle

The top edge of the playback rectangle. You can also set this value.

**See also:** [VideoOverlay.left](VideoOverlay.md#left) / [VideoOverlay.setPos](VideoOverlay.md#setpos)

---

### visible

Property \ Access: `r/w`

**Description**

Whether visible

Specifies whether the playback area is visible. You can also set this value.

True means visible; false means invisible.

---

### fps

Property \ Access: `r`

**Description**

Frame rate

The frame rate (frames per second).

For WebM files that have no frame rate recorded (or have an invalid value below 1 fps), this is 0,
and in that case frame / numberOfFrame are also 0.

---

### numberOfFrame

Property \ Access: `r`

**Description**

Total number of frames

The total number of frames.

---

### totalTime

Property \ Access: `r`

**Description**

Total time

The total time in ms.

---

### layer1

Property \ Access: `r/w`

**Description**

Drawing layer 1

The layer to draw to in layer drawing mode. You can also set this value.

By setting the layer1 and layer2 properties to different layers, you can show the same movie on two layers at the same time.

---

### layer2

Property \ Access: `r/w`

**Description**

Drawing layer 2

The layer to draw to in layer drawing mode. You can also set this value.

---

### mode

Property \ Access: `r/w`

**Description**

Playback mode

The playback method. Set it before opening (changes after opening have no effect).

- **vomOverlay** (default, overlay): shows the movie full-screen in front. On Windows,
mp4/H.264/HEVC/wmv/asf and similar formats use hardware decoding (Media Foundation's
IMFMediaEngine) by default, and the video is composited directly into the Direct3D11 back
buffer of the draw device (BasicDrawDevice). webm/mpeg use software decoding. In this mode,
no additional image compositing with {@link VideoOverlay.setMixingLayer setMixingLayer} is performed.
- **vomMixer** (mixer): overlay plus additional image compositing. It does not use hardware decoding and
always takes the software compositing path, so image compositing with {@link VideoOverlay.setMixingLayer setMixingLayer}
is available (audio is also processed internally, so volume control reliably takes effect).
- **vomLayer** (layer drawing): draws the movie as the image of a layer ({@link VideoOverlay.layer1 layer1} /
{@link VideoOverlay.layer2 layer2}).
- **vomMFEVR**: the former Media Foundation + EVR mode. It now behaves the same as vomOverlay
(the value is kept for compatibility).

Hardware decoding can be disabled with the command-line option **-mediaengine=no**, in which
case all formats are software-decoded.

---

### playRate

Property \ Access: `r/w`

**Description**

Playback rate

Sets the playback rate of the media.

1.0 is normal speed, 0.5 is half speed, and 2 is double speed.

The range that can be set depends on the decoder / codec.

For reference: for movies with audio, values from just above 0.0 up to about 2.0 can generally be set. For movies without audio, any value greater than 0.0 within the range of a double can be set, but the actual playback speed is capped by processing speed.

---

### segmentLoopStartFrame

Property \ Access: `r`

**Description**

Start frame of the segment loop

The start frame of the segment loop.

**See also:** [VideoOverlay.setSegmentLoop](VideoOverlay.md#setsegmentloop) / [VideoOverlay.cancelSegmentLoop](VideoOverlay.md#cancelsegmentloop)

---

### segmentLoopEndFrame

Property \ Access: `r`

**Description**

End frame of the segment loop

The end frame of the segment loop.

**See also:** [VideoOverlay.setSegmentLoop](VideoOverlay.md#setsegmentloop)

---

### periodEventFrame

Property \ Access: `r/w`

**Description**

Period event frame

The frame at which to raise the period event.

Negative if not set.

---

### audioBalance

Property \ Access: `r/w`

**Description**

Audio balance (panning)

The pan (stereo position). You can also set this value.

Specifies the left/right position from which the sound is heard.

Specify a number from -100000 through 0 to 100000, where -100000 is fully left, 0 is center, and 100000 is fully right.

When playing a stereo source, panning is achieved by attenuating either the left or the right channel (0 outputs both channels, and -100000 outputs only the left channel).

---

### audioVolume

Property \ Access: `r/w`

**Description**

Audio volume

The playback volume. You can also set this value.

Specify a number from 0 to 100000, where 0 is fully muted and 100000 is 100% volume.

---

### numberOfAudioStream

Property \ Access: `r`

**Description**

Number of audio streams

Available only for MPEG files.
Gets the number of audio streams.

**See also:** [VideoOverlay.selectAudioStream](VideoOverlay.md#selectaudiostream) / [VideoOverlay.enabledAudioStream](VideoOverlay.md#enabledaudiostream)

---

### enabledAudioStream

Property \ Access: `r`

**Description**

Audio stream number being played

Available only for MPEG files.
Gets the number of the audio stream being played.
Returns -1 if no audio stream is found.

**See also:** [VideoOverlay.selectAudioStream](VideoOverlay.md#selectaudiostream) / [VideoOverlay.numberOfAudioStream](VideoOverlay.md#numberofaudiostream)

---

### mixingMovieAlpha

Property \ Access: `r/w`

**Description**

Video transparency

The transparency of the video, from 0.0 (fully transparent) to 1.0 (fully opaque).

Available only in mixer mode.

---

### mixingMovieBGColor

Property \ Access: `r/w`

**Description**

Video background color

The background color of the video.

Available only in mixer mode.

---

### contrastRangeMin

Property \ Access: `r`

**Description**

Minimum of the video contrast range

The minimum of the contrast range.

Available only in mixer mode.

---

### contrastRangeMax

Property \ Access: `r`

**Description**

Maximum of the video contrast range

The maximum of the contrast range.

Available only in mixer mode.

---

### contrastDefaultValue

Property \ Access: `r`

**Description**

Default video contrast

The default contrast value.

Available only in mixer mode.

---

### contrastStepSize

Property \ Access: `r`

**Description**

Step size for video contrast

The valid increment from contrastRangeMin to contrastRangeMax.

The contrast can be changed in units of this value.

Available only in mixer mode.

---

### contrast

Property \ Access: `r/w`

**Description**

Video contrast

The contrast of the video.

Available only in mixer mode.

---

### brightnessRangeMin

Property \ Access: `r`

**Description**

Minimum of the video brightness range

The minimum of the brightness range.

Available only in mixer mode.

---

### brightnessRangeMax

Property \ Access: `r`

**Description**

Maximum of the video brightness range

The maximum of the brightness range.

Available only in mixer mode.

---

### brightnessDefaultValue

Property \ Access: `r`

**Description**

Default video brightness

The default brightness value.

Available only in mixer mode.

---

### brightnessStepSize

Property \ Access: `r`

**Description**

Step size for video brightness

The valid increment from brightnessRangeMin to brightnessRangeMax.

The brightness can be changed in units of this value.

Available only in mixer mode.

---

### brightness

Property \ Access: `r/w`

**Description**

Video brightness

The brightness of the video.

Available only in mixer mode.

---

### hueRangeMin

Property \ Access: `r`

**Description**

Minimum of the video hue range

The minimum of the hue range.

Available only in mixer mode.

---

### hueRangeMax

Property \ Access: `r`

**Description**

Maximum of the video hue range

The maximum of the hue range.

Available only in mixer mode.

---

### hueDefaultValue

Property \ Access: `r`

**Description**

Default video hue

The default hue value.

Available only in mixer mode.

---

### hueStepSize

Property \ Access: `r`

**Description**

Step size for video hue

The valid increment from hueRangeMin to hueRangeMax.

The hue can be changed in units of this value.

Available only in mixer mode.

---

### hue

Property \ Access: `r/w`

**Description**

Video hue

The hue of the video.

Available only in mixer mode.

---

### saturationRangeMin

Property \ Access: `r`

**Description**

Minimum of the video saturation range

The minimum of the saturation range.

Available only in mixer mode.

---

### saturationRangeMax

Property \ Access: `r`

**Description**

Maximum of the video saturation range

The maximum of the saturation range.

Available only in mixer mode.

---

### saturationDefaultValue

Property \ Access: `r`

**Description**

Default video saturation

The default saturation value.

Available only in mixer mode.

---

### saturationStepSize

Property \ Access: `r`

**Description**

Step size for video saturation

The valid increment from saturationRangeMin to saturationRangeMax.

The saturation can be changed in units of this value.

Available only in mixer mode.

---

### saturation

Property \ Access: `r/w`

**Description**

Video saturation

The saturation of the video.

Available only in mixer mode.

---

### originalWidth

Property \ Access: `r`

**Description**

Actual width of the video

The width of the stored video.

---

### originalHeight

Property \ Access: `r`

**Description**

Actual height of the video

The height of the stored video.

---

### enabledVideoStream

Property \ Access: `r/w`

**Type**: `Integer`

**Description**

Index of the enabled video stream

Gets or sets the index of the video stream currently used for playback.
Setting it calls `SelectVideoStream` and switches to the corresponding stream.

**See also:** [VideoOverlay.numberOfVideoStream](VideoOverlay.md#numberofvideostream)

---

### numberOfVideoStream

Property \ Access: `r/w`

**Type**: `Integer`

**Description**

Number of video streams

Returns the number of video streams in the open movie. Read-only.

**See also:** [VideoOverlay.enabledVideoStream](VideoOverlay.md#enabledvideostream)

---

### open

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `storage` | `&nbsp;` | The media to open. |

**Description**

Opens media

Opens the specified media.

The main playable formats are WebM (VP8/VP9, with alpha support), MPEG-1 (extensions .mpeg / .mpg / .mpv),
WMV / ASF, MP4 (.mp4 / .m4v / .mov, H.264 / HEVC), and AVI (depending on the internal codec).

WebM supports movies with transparency (alpha). MP4 / WMV and similar formats are hardware-decoded by default.

By specification, MPEG-1 frame rates are limited to 23.976 / 24 / 25 / 29.97 / 30 / 50 / 59.94 / 60 fps.
For material with a low frame rate such as 8 fps, repeat frames to reach 24 fps or similar before converting.

`"stop"` is also delivered to onStatusChanged when the media is opened. When detecting the end of playback,
treat only a `"stop"` that follows `"play"` as the end.

---

### play

Method

**Description**

Starts playback

Starts playing the media.

If paused, playback resumes from where it was; after stopping or after playing to the end, it starts from the beginning.

---

### stop

Method

**Description**

Stops playback

Stops playing the media.

---

### pause

Method

**Description**

Pauses playback

Pauses playing the media.

---

### rewind

Method

**Description**

Rewinds

Moves the playback position of the media to the beginning.

---

### prepare

Method

**Description**

Prepares playback

Draws the first frame of the media to the specified layer and raises an onPeriod event when drawing finishes.
After calling the prepare method, wait for the onPeriod event before starting playback.

Meaningful only when mode is `vomLayer` (layer mode).

No audio is played during preparation. When preparation finishes, the media is stopped at the beginning,
so calling play after receiving onPeriod (perPrepare) plays from the beginning.

**See also:** [VideoOverlay.onPeriod](VideoOverlay.md#onperiod)

---

### setSegmentLoop

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `comeFrame` | `&nbsp;` | The loop destination frame (the start frame of the loop). When playback reaches goFrame, the playhead moves to this frame. |
| `goFrame` | `&nbsp;` | The loop end frame. When the frame just before this one has finished displaying, the playhead moves to comeFrame. |

**Description**

Sets a loop between frames

Loops between the specified frames.

An onPeriod event occurs at the loop end (goFrame).

The frame at comeFrame must be a keyframe in the movie file.

If it is not,
when moving from the loop end to the loop start, the playback position moves to the keyframe closest to the specified frame.

**See also:** [VideoOverlay.cancelSegmentLoop](VideoOverlay.md#cancelsegmentloop) / [VideoOverlay.onPeriod](VideoOverlay.md#onperiod) / [VideoOverlay.segmentLoopStartFrame](VideoOverlay.md#segmentloopstartframe) / [VideoOverlay.segmentLoopEndFrame](VideoOverlay.md#segmentloopendframe)

---

### cancelSegmentLoop

Method

**Description**

Cancels the loop between frames

Cancels the segment loop set with the setSegmentLoop method.

**See also:** [VideoOverlay.setSegmentLoop](VideoOverlay.md#setsegmentloop)

---

### close

Method

**Description**

Closes the media

Closes the media.

All resources allocated for playing the media are also released.

**See also:** [VideoOverlay.setSegmentLoop](VideoOverlay.md#setsegmentloop)

---

### setPeriodEvent

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `eventFrame` | `&nbsp;` | The frame at which to raise the onPeriod event. |

**Description**

Requests an event at a specified frame

Raises an onPeriod event at the specified frame.

Once the onPeriod event occurs, the request is cleared. To raise it again, set it again with this method.

**See also:** [VideoOverlay.cancelPeriodEvent](VideoOverlay.md#cancelperiodevent) / [VideoOverlay.onPeriod](VideoOverlay.md#onperiod)

---

### cancelPeriodEvent

Method

**Description**

Cancels the event at a specified frame

Cancels the event set with the setPeriodEvent method.

**See also:** [VideoOverlay.setPeriodEvent](VideoOverlay.md#setperiodevent)

---

### setPos

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `left` | `&nbsp;` | Left edge of the rectangular area used to play the media. |
| `top` | `&nbsp;` | Top edge of the rectangular area used to play the media. |

**Description**

Sets the top-left position of the playback rectangle

Sets the top-left position of the rectangular area used to play the media.

Coordinates are in pixels, relative to the window's client area (the area where layers can be
displayed).

> In overlay / mixer playback (vomOverlay / vomMixer), while none of the playback rectangle settings (setPos / setSize / setBounds / left / top / width / height) have been specified, the movie is shown over the whole screen. Once specified, it is shown in that rectangle over the game screen. The coordinates are primary layer coordinates and are mapped to the display following the window's scaling.

---

### setSize

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `width` | `&nbsp;` | Width of the rectangular area used to play the media. |
| `height` | `&nbsp;` | Height of the rectangular area used to play the media. |

**Description**

Sets the size of the playback rectangle

Sets the size, in pixels, of the rectangular area used to play the media.

In the current version, this method cannot be used during layer playback.

> In overlay / mixer playback (vomOverlay / vomMixer), while none of the playback rectangle settings (setPos / setSize / setBounds / left / top / width / height) have been specified, the movie is shown over the whole screen. Once specified, it is shown in that rectangle over the game screen. The coordinates are primary layer coordinates and are mapped to the display following the window's scaling.

---

### setBounds

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `left` | `&nbsp;` | Left edge of the rectangular area used to play the media. |
| `top` | `&nbsp;` | Top edge of the rectangular area used to play the media. |
| `width` | `&nbsp;` | Width of the rectangular area used to play the media. |
| `height` | `&nbsp;` | Height of the rectangular area used to play the media. |

**Description**

Sets the position and size of the playback rectangle

Sets the position and size of the rectangular area used to play the media.

Coordinates are in pixels, relative to the window's client area (the area where layers can be
displayed).

In the current version, during layer playback only the position can be set with this method; the size is ignored.

> In overlay / mixer playback (vomOverlay / vomMixer), while none of the playback rectangle settings (setPos / setSize / setBounds / left / top / width / height) have been specified, the movie is shown over the whole screen. Once specified, it is shown in that rectangle over the game screen. The coordinates are primary layer coordinates and are mapped to the display following the window's scaling.

---

### selectAudioStream

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `streamNumber` | `&nbsp;` | The audio stream number. |

**Description**

Selects an audio stream

Enables the specified audio stream number.

Cannot be used with videos that do not contain multiple audio streams.

**See also:** [VideoOverlay.numberOfAudioStream](VideoOverlay.md#numberofaudiostream) / [VideoOverlay.enabledAudioStream](VideoOverlay.md#enabledaudiostream)

---

### setMixingLayer

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `layer` | `&nbsp;` | The layer. |

**Description**

Sets the layer to mix

Mixes the specified layer with the video.

Mixing uses the layer image as it was when this method was called.

To reflect updates to the layer image, you need to call this method again.

If you use VideOverlay.OnFrameUpdate to detect
that the layer image has been updated and call this method then, updates are reflected automatically.
Calling this method every frame from onFrameUpdate puts a considerable load on the system, so avoid doing that.

Available only in mixer mode.

---

### resetMixingLayer

Method

**Description**

Clears the layer to mix

Stops mixing the video with the layer.

Available only in mixer mode.

---

### onStatusChanged

Event

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `status` | `&nbsp;` | The status string.<br>One of the following.<br>`"**unload**"   : ` no media is open<br>`"**ready**"    : ` the media is ready<br>`"**play**"     : ` the media is playing<br>`"**stop**"     : ` the media is stopped<br>`"**pause**"    : ` the media is paused |

**Description**

The status changed

Occurs when the status of this object changes.

ready occurs only in vomMFEVR mode.

---

### onPeriod

Event

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `type` | `&nbsp;` | The type of the period event.<br>One of the following.<br>`**perLoop**    : ` the end of a (normal) loop was reached. Occurs once per cycle, at the point where playback rewinds to the beginning<br>after the last frame has been shown for one frame<br>`**perSegLoop** : ` the end of a segment loop was reached<br>`**perPeriod**  : ` the frame specified with the setPeriodEvent method was reached<br>`**perPrepare** : ` playback preparation by the prepare method completed |

**Description**

A period event occurred

Called when the end of a loop or the frame specified with setPeriodEvent is reached, or when playback preparation by the prepare method completes.

When this event is called because the end of a loop or the frame specified with setPeriodEvent was reached, the playback position may already be past the specified position, depending on playback conditions. To get the actual current playback position, read the frame property.

**See also:** [VideoOverlay.setPeriodEvent](VideoOverlay.md#setperiodevent) / [VideoOverlay.prepare](VideoOverlay.md#prepare) / [VideoOverlay.frame](VideoOverlay.md#frame)

---

### onFrameUpdate

Event

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `frame` | `&nbsp;` | The video frame number. |

**Description**

The video frame was updated

Called after the video frame is updated.

The frame argument does not necessarily match the video frame currently displayed exactly.

It also occurs when the first frame (frame 0) is shown. Frame numbers count the first frame as 0
(even for material whose timestamps start after 0, such as MP4, the first frame is 0).

Available only in layer drawing mode and mixer mode.

---

### onCallbackCommand

Event

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `command` | `&nbsp;` | The command name. |
| `arg` | `&nbsp;` | The argument accompanying the command. |

**Description**

Custom command callback (event)

An event that fires when an arbitrary command notification is received from the movie player.

---

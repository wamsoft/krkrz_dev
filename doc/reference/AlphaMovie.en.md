# AlphaMovie

Manual written as pseudo-code

Kirikiri Z AlphaMovie plugin.

Plays the .amv (Alpha Movie) container, a movie format with an alpha channel, and draws each frame
directly over the main image buffer of the target Layer (including alpha).

Example:
var mov = new AlphaMovie();
mov.open("video/explosion.amv");
mov.setPosition(100, 80);
mov.loop = true;
// every frame:
var no = mov.showNextImage(layer);

Each call to showNextImage advances one frame and returns the number of the frame it drew.
At the end, it rewinds to the beginning if loop=true. If loop=false, it keeps returning the last
frame number (or moves on to the next movie automatically if one was queued with setNextMovieFile).
Each frame overwrites only its own rectangle (left, top, width, height),
so areas that are not drawn keep the previous frame's content on the Layer.

## Members

### Constructors

- [AlphaMovie](#alphamovie)

### Properties

- [numOfFrame](#numofframe)
- [frame](#frame)
- [loop](#loop)
- [nextLoop](#nextloop)
- [preloadSamples](#preloadsamples)
- [left](#left)
- [top](#top)
- [screenWidth](#screenwidth)
- [screenHeight](#screenheight)
- [FPSScale](#fpsscale)
- [FPSRate](#fpsrate)

### Methods

- [open](#open)
- [clear](#clear)
- [showNextImage](#shownextimage)
- [isPlaying](#isplaying)
- [play](#play)
- [stop](#stop)
- [setPosition](#setposition)
- [setNextMovieFile](#setnextmoviefile)

---

### AlphaMovie

Constructor

**Description**

Constructor (no arguments)

---

### numOfFrame

Property \ Access: `r`

**Description**

Total number of frames (read-only)

---

### frame

Property \ Access: `r/w`

**Description**

Current frame number. Setting it seeks to that position

---

### loop

Property \ Access: `r/w`

**Description**

Whether to loop playback

---

### nextLoop

Property \ Access: `r/w`

**Description**

Loop setting for the next movie (setNextMovieFile)

---

### preloadSamples

Property \ Access: `r/w`

**Description**

Number of read-ahead buffers (this implementation only stores the value; default 5)

---

### left

Property \ Access: `r/w`

**Description**

Display position, left (= X of setPosition)

---

### top

Property \ Access: `r/w`

**Description**

Display position, top (= Y of setPosition)

---

### screenWidth

Property \ Access: `r`

**Description**

Width of the movie (read-only)

---

### screenHeight

Property \ Access: `r`

**Description**

Height of the movie (read-only)

---

### FPSScale

Property \ Access: `r`

**Description**

Numerator of the frame rate. FPS = FPSScale / FPSRate (read-only)

---

### FPSRate

Property \ Access: `r`

**Description**

Denominator of the frame rate. FPS = FPSScale / FPSRate (read-only)

---

### open

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `filename` | `&nbsp;` | Target storage (.amv). |

**Description**

Opens an amv file

---

### clear

Method

**Description**

Clears the queue of decoded frames (a no-op, since this implementation decodes synchronously)

---

### showNextImage

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `layer` | `&nbsp;` | Destination Layer (must have hasImage). |

**Return value**

Number of the frame drawn (integer).

**Description**

Draws the next frame onto the target Layer

---

### isPlaying

Method

**Return value**

true: playing / false: stopped.

**Description**

Returns whether the movie is playing

---

### play

Method

**Description**

Starts playback (rewinds to the first frame and enters the playing state)

---

### stop

Method

**Description**

Stops playback

---

### setPosition

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `x` | `&nbsp;` | Display position X. |
| `y` | `&nbsp;` | Display position Y. |

**Description**

Sets the display position (top-left)

---

### setNextMovieFile

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `filename` | `&nbsp;` | amv storage to play next. |

**Description**

Queues the next amv to play (switches automatically when the current movie ends)

---

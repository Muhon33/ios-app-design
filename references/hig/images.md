# Images
_To make sure your artwork looks great on all devices you support, learn how the system displays content and how to deliver art at the appropriate scale factors._
Source: https://developer.apple.com/design/human-interface-guidelines/images

### Resolution
- **Provide high-resolution assets for all bitmap images in your app, for every device you support.** As you add each image to your project’s asset catalog, identify its scale factor by appending “@1x,” “@2x,” or “@3x” to its filename. Use the following values for guidance; for additional scale factors, see Layout.

| Platform | Scale factors |
|---|---|
| iPadOS, watchOS | @2x |
| iOS | @2x and @3x |
| visionOS | @2x or higher (see visionOS) |
| macOS, tvOS | @1x and @2x |

- **In general, design images at the lowest resolution and scale them up to create high-resolution assets.** When you use resizable vectorized shapes, you might want to position control points at whole values so that they’re cleanly aligned at 1x. This positioning allows the points to remain cleanly aligned to the raster grid at higher resolutions, because 2x and 3x are multiples of 1x.

### Formats

| Image type | Format |
|---|---|
| Bitmap or raster work | De-interlaced PNG files |
| PNG graphics that don’t require full 24-bit color | An 8-bit color palette |
| Photos | JPEG files, optimized as necessary, or HEIC files |
| Stereo or spatial photos | Stereo HEIC |
| Flat icons, interface icons, and other flat artwork that requires high-resolution scaling | PDF or SVG files |


### Best practices
- **Include a color profile with each image.** Color profiles help ensure that your app’s colors appear as intended on different displays. For guidance, see Color management.
- **Always test images on a range of actual devices.** An image that looks great at design time may appear pixelated, stretched, or compressed when viewed on various devices.

### Platform considerations
No additional considerations for iOS, iPadOS, or macOS.

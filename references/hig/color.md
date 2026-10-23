# Color
_Judicious use of color can enhance communication, evoke your brand, provide visual continuity, communicate status and feedback, and help people understand information._
Source: https://developer.apple.com/design/human-interface-guidelines/color

### Best practices
- **Avoid using the same color to mean different things.** Use color consistently throughout your interface, especially when you use it to help communicate information like status or interactivity. For example, if you use your brand color to indicate that a borderless button is interactive, using the same or similar color to stylize noninteractive text is confusing.
- **Make sure all your app’s colors work well in light, dark, and increased contrast contexts.** iOS, iPadOS, macOS, and tvOS offer both light and dark appearance settings. System colors vary subtly depending on the system appearance, adjusting to ensure proper color differentiation and contrast for text, symbols, and other elements. With the Increase Contrast setting turned on, the color differences become far more apparent. When possible, use system colors, which already define variants for all these contexts. If you define a custom color, make sure to supply light and dark variants, and an increased contrast option for each variant that provides a significantly higher amount of visual differentiation. Even if your app ships in a single appearance mode, provide both light and dark colors to support Liquid Glass adaptivity in these contexts.
- **Test your app’s color scheme under a variety of lighting conditions.** Colors can look different when you view your app outside on a sunny day or in dim light. In bright surroundings, colors look darker and more muted. In dark environments, colors appear bright and saturated. In visionOS, colors can look different depending on the colors of a wall or object in a person’s physical surroundings and how it reflects light. Adjust app colors to provide an optimal viewing experience in the majority of use cases.
- **Test your app on different devices.** For example, the True Tone display — available on certain iPhone, iPad, and Mac models — uses ambient light sensors to automatically adjust the white point of the display to adapt to the lighting conditions of the current environment. Apps that primarily support reading, photos, video, and gaming can strengthen or weaken this effect by specifying a white point adaptivity style (for developer guidance, see UIWhitePointAdaptivityStyle). Test tvOS apps on multiple brands of HD and 4K TVs, and with different display settings. You can also test the appearance of your app using different color profiles on a Mac — such as P3 and Standard RGB (sRGB) — by choosing a profile in System Settings > Displays. For guidance, see Color management.
- **Consider how artwork and translucency affect nearby colors.** Variations in artwork sometimes warrant changes to nearby colors to maintain visual continuity and prevent interface elements from becoming overpowering or underwhelming. Maps, for example, displays a light color scheme when in map mode but switches to a dark color scheme when in satellite mode. Colors can also appear different when placed behind or applied to a translucent element like a toolbar.
- **If your app lets people choose colors, prefer system-provided color controls where available.** Using built-in color pickers provides a consistent user experience, in addition to letting people save a set of colors they can access from any app. For developer guidance, see ColorPicker.

### Inclusive color
- **Avoid relying solely on color to differentiate between objects, indicate interactivity, or communicate essential information.** When you use color to convey information, be sure to provide the same information in alternative ways so people with color blindness or other visual disabilities can understand it. For example, you can use text labels or glyph shapes to identify objects or states.
- **Avoid using colors that make it hard to perceive content in your app.** For example, insufficient contrast can cause icons and text to blend with the background and make content hard to read, and people who are color blind might not be able to distinguish some color combinations. For guidance, see Accessibility.
- **Consider how the colors you use might be perceived in other countries and cultures.** For example, red communicates danger in some cultures, but has positive connotations in other cultures. Make sure the colors in your app send the message you intend.

### System colors
- **Avoid hard-coding system color values in your app.** Documented color values are for your reference during the app design process. The actual color values may fluctuate from release to release, based on a variety of environmental variables. Use APIs like Color to apply system colors.
- **Avoid redefining the semantic meanings of dynamic system colors.** To ensure a consistent experience and ensure your interface looks great when the appearance of the platform changes, use dynamic system colors as intended. For example, don’t use the separator color as a text color, or secondary text label color as a background color.

### Liquid Glass color
- **Apply color sparingly to the Liquid Glass material, and to symbols or text on the material.** If you apply color, reserve it for elements that truly benefit from emphasis, such as status indicators or primary actions. To emphasize primary actions, apply color to the background rather than to symbols or text. For example, the system applies the app accent color to the background in prominent buttons — such as the Done button — to draw attention and elevate their visual prominence. Refrain from adding color to the background of multiple controls.
- **Avoid using similar colors in control labels if your app has a colorful background.** While color can make apps more visually appealing, playful, or reflective of your brand, too much color can be overwhelming and make control labels more difficult to read. If your app features colorful backgrounds or visually rich content, prefer a monochromatic appearance for toolbars and tab bars, or choose an accent color with sufficient visual differentiation. By contrast, in apps with primarily monochromatic content or backgrounds, choosing your brand color as the app accent color can be an effective way to tailor your app experience and reflect your company’s identity.
- **Be aware of the placement of color in the content layer.** Make sure your interface maintains sufficient contrast by avoiding overlap of similar colors in the content layer and controls when possible. Although colorful content might intermittently scroll underneath controls, make sure its default or resting state — like the top of a screen of scrollable content — maintains clear legibility.

### Color management
- **Apply color profiles to your images.** Color profiles help ensure that your app’s colors appear as intended on different displays. The sRGB color space produces accurate colors on most displays.
- **Use wide color to enhance the visual experience on compatible displays.** Wide color displays support a P3 color space, which can produce richer, more saturated colors than sRGB. As a result, photos and videos that use wide color are more lifelike, and visual data and status indicators that use wide color can be more meaningful. When appropriate, use the Display P3 color profile at 16 bits per pixel (per channel) and export images in PNG format. Note that you need to use a wide color display to design wide color images and select P3 colors.
- **Provide color space–specific image and color variations if necessary.** In general, P3 colors and images appear fine on sRGB displays. Occasionally, it may be hard to distinguish two very similar P3 colors when viewing them on an sRGB display. Gradients that use P3 colors can also sometimes appear clipped on sRGB displays. To avoid these issues and to ensure visual fidelity on both wide color and sRGB displays, you can use the asset catalog of your Xcode project to provide different versions of images and colors for each color space.

### Platform considerations

#### iOS, iPadOS
iOS defines two sets of dynamic background colors — system and grouped — each of which contains primary, secondary, and tertiary variants that help you convey a hierarchy of information. In general, use the grouped background colors (systemGroupedBackground, secondarySystemGroupedBackground, and tertiarySystemGroupedBackground) when you have a grouped table view; otherwise, use the system set of background colors (systemBackground, secondarySystemBackground, and tertiarySystemBackground).
With both sets of background colors, you generally use the variants to indicate hierarchy in the following ways:
  - Primary for the overall view
  - Secondary for grouping content or elements within the overall view
  - Tertiary for grouping content or elements within secondary elements
For foreground content, iOS defines the following dynamic colors:

| Color | Use for… | UIKit API |
|---|---|---|
| Label | A text label that contains primary content. | label |
| Secondary label | A text label that contains secondary content. | secondaryLabel |
| Tertiary label | A text label that contains tertiary content. | tertiaryLabel |
| Quaternary label | A text label that contains quaternary content. | quaternaryLabel |
| Placeholder text | Placeholder text in controls or text views. | placeholderText |
| Separator | A separator that allows some underlying content to be visible. | separator |
| Opaque separator | A separator that doesn’t allow any underlying content to be visible. | opaqueSeparator |
| Link | Text that functions as a link. | link |


### Specifications

#### System colors

| Name | SwiftUI API | Default (light) | Default (dark) | Increased contrast (light) | Increased contrast (dark) |
|---|---|---|---|---|---|
| Red | red | 255,56,60 #FF383C | 255,66,69 #FF4245 | 233,21,45 #E9152D | 255,97,101 #FF6165 |
| Orange | orange | 255,141,40 #FF8D28 | 255,146,48 #FF9230 | 197,83,0 #C55300 | 255,160,86 #FFA056 |
| Yellow | yellow | 255,204,0 #FFCC00 | 255,214,0 #FFD600 | 161,106,0 #A16A00 | 254,223,67 #FEDF43 |
| Green | green | 52,199,89 #34C759 | 48,209,88 #30D158 | 0,137,50 #008932 | 74,217,104 #4AD968 |
| Mint | mint | 0,200,179 #00C8B3 | 0,218,195 #00DAC3 | 0,133,117 #008575 | 84,223,203 #54DFCB |
| Teal | teal | 0,195,208 #00C3D0 | 0,210,224 #00D2E0 | 0,129,152 #008198 | 59,221,236 #3BDDEC |
| Cyan | cyan | 0,192,232 #00C0E8 | 60,211,254 #3CD3FE | 0,126,174 #007EAE | 109,217,255 #6DD9FF |
| Blue | blue | 0,136,255 #0088FF | 0,145,255 #0091FF | 30,110,244 #1E6EF4 | 92,184,255 #5CB8FF |
| Indigo | indigo | 97,85,245 #6155F5 | 109,124,255 #6D7CFF | 86,74,222 #564ADE | 167,170,255 #A7AAFF |
| Purple | purple | 203,48,224 #CB30E0 | 219,52,242 #DB34F2 | 176,47,194 #B02FC2 | 234,141,255 #EA8DFF |
| Pink | pink | 255,45,85 #FF2D55 | 255,55,95 #FF375F | 231,18,77 #E7124D | 255,138,196 #FF8AC4 |
| Brown | brown | 172,127,94 #AC7F5E | 183,138,102 #B78A66 | 149,109,81 #956D51 | 219,166,121 #DBA679 |


#### iOS, iPadOS system gray colors

| Name | UIKit API | Default (light) | Default (dark) | Increased contrast (light) | Increased contrast (dark) |
|---|---|---|---|---|---|
| Gray | systemGray | 142,142,147 #8E8E93 | 142,142,147 #8E8E93 | 108,108,112 #6C6C70 | 174,174,178 #AEAEB2 |
| Gray (2) | systemGray2 | 174,174,178 #AEAEB2 | 99,99,102 #636366 | 142,142,147 #8E8E93 | 124,124,128 #7C7C80 |
| Gray (3) | systemGray3 | 199,199,204 #C7C7CC | 72,72,74 #48484A | 174,174,178 #AEAEB2 | 84,84,86 #545456 |
| Gray (4) | systemGray4 | 209,209,214 #D1D1D6 | 58,58,60 #3A3A3C | 188,188,192 #BCBCC0 | 68,68,70 #444446 |
| Gray (5) | systemGray5 | 229,229,234 #E5E5EA | 44,44,46 #2C2C2E | 216,216,220 #D8D8DC | 54,54,56 #363638 |
| Gray (6) | systemGray6 | 242,242,247 #F2F2F7 | 28,28,30 #1C1C1E | 235,235,240 #EBEBF0 | 36,36,38 #242426 |

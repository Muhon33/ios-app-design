# Materials
_A material is a visual effect that creates a sense of depth, layering, and hierarchy between foreground and background elements._
Source: https://developer.apple.com/design/human-interface-guidelines/materials

### Liquid Glass
- **Don’t use Liquid Glass in the content layer.** Liquid Glass works best when it provides a clear distinction between interactive elements and content, and including it in the content layer can result in unnecessary complexity and a confusing visual hierarchy. Instead, use standard materials for elements in the content layer, such as app backgrounds. An exception to this is for controls in the content layer with a transient interactive element like sliders and toggles; in these cases, the element takes on a Liquid Glass appearance to emphasize its interactivity when a person activates it.
- **Use Liquid Glass effects sparingly.** Standard components from system frameworks pick up the appearance and behavior of this material automatically. If you apply Liquid Glass effects to a custom control, do so sparingly. Liquid Glass seeks to bring attention to the underlying content, and overusing this material in multiple custom controls can provide a subpar user experience by distracting from that content. Limit these effects to the most important functional elements in your app. For developer guidance, see Applying Liquid Glass to custom views.
- **Only use clear Liquid Glass for components that appear over visually rich backgrounds.** Liquid Glass provides two variants — regular and clear — that you can choose when building custom components or styling some system components. The appearance of these variants can differ in response to certain system settings, like if people choose a preferred look for Liquid Glass in their device’s settings, or turn on accessibility settings that reduce transparency or increase contrast in the interface.
  - If the underlying content is bright, consider adding a dark dimming layer of 35% opacity. For developer guidance, see clear.
  - If the underlying content is sufficiently dark, or if you use standard media playback controls from AVKit that provide their own dimming layer, you don’t need to apply a dimming layer.

### Standard materials
- **Choose materials and effects based on semantic meaning and recommended usage.** Avoid selecting a material or effect based on the apparent color it imparts to your interface, because system settings can change its appearance and behavior. Instead, match the material or vibrancy style to your specific use case.
- **Help ensure legibility by using vibrant colors on top of materials.** When you use system-defined vibrant colors, you don’t need to worry about colors seeming too dark, bright, saturated, or low contrast in different contexts. Regardless of the material you choose, use vibrant colors on top of it. For guidance, see System colors.
- **Consider contrast and visual separation when choosing a material to combine with blur and vibrancy effects.** For example, consider that:
  - Thicker materials, which are more opaque, can provide better contrast for text and other elements with fine features.
  - Thinner materials, which are more translucent, can help people retain their context by providing a visible reminder of the content that’s in the background.

### Platform considerations

#### iOS, iPadOS
In addition to Liquid Glass, iOS and iPadOS continue to provide four standard materials — ultra-thin, thin, regular (default), and thick — which you can use in the content layer to help create visual distinction.
iOS and iPadOS also define vibrant colors for labels, fills, and separators that are specifically designed to work with each material. Labels and fills both have several levels of vibrancy; separators have one level. The name of a level indicates the relative amount of contrast between an element and the background: The default level has the highest contrast, whereas quaternary (when it exists) has the lowest contrast.
Except for quaternary, you can use the following vibrancy values for labels on any material. In general, avoid using quaternary on top of the thin and ultraThin materials, because the contrast is too low.
  - UIVibrancyEffectStyle.label (default)
  - UIVibrancyEffectStyle.secondaryLabel
  - UIVibrancyEffectStyle.tertiaryLabel
  - UIVibrancyEffectStyle.quaternaryLabel
You can use the following vibrancy values for fills on all materials.
  - UIVibrancyEffectStyle.fill (default)
  - UIVibrancyEffectStyle.secondaryFill
  - UIVibrancyEffectStyle.tertiaryFill
The system provides a single, default vibrancy value for a separator, which works well on all materials.

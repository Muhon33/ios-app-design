# Text views
_A text view displays multiline, styled text content, which can optionally be editable._
Source: https://developer.apple.com/design/human-interface-guidelines/text-views

### Best practices
- **Use a text view when you need to display text that’s long, editable, or in a special format.** Text views differ from text fields and labels in that they provide the most options for displaying specialized text and receiving text input. If you need to display a small amount of text, it’s simpler to use a label or — if the text is editable — a text field.
- **Keep text legible.** Although you can use multiple fonts, colors, and alignments in creative ways, it’s essential to maintain the readability of your content. It’s a good idea to adopt Dynamic Type so your text still looks good if people change text size on their device. Be sure to test your content with accessibility options turned on, such as bold text. For guidance, see Accessibility and Typography.
- **Make useful text selectable.** If a text view contains useful information such as an error message, a serial number, or an IP address, consider letting people select and copy it for pasting elsewhere.

### Platform considerations
No additional considerations for macOS, visionOS, or watchOS.

#### iOS, iPadOS
- **Show the appropriate keyboard type.** Several different keyboard types are available, each designed to facilitate a different type of input. To streamline data entry, the keyboard you display when editing a text view needs to be appropriate for the type of content. For guidance, see Virtual keyboards.

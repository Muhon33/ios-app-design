# Disclosure controls
_Disclosure controls reveal and hide information and functionality related to specific controls or views._
Source: https://developer.apple.com/design/human-interface-guidelines/disclosure-controls

### Best practices
- **Use a disclosure control to hide details until they’re relevant.** Place controls that people are most likely to use at the top of the disclosure hierarchy so they’re always visible, with more advanced functionality hidden by default. This organization helps people quickly find the most essential information without overwhelming them with too many detailed options.

### Disclosure triangles
- **Provide a descriptive label when using a disclosure triangle.** Make sure your labels indicate what is disclosed or hidden, like “Advanced Options.”

### Disclosure buttons
- **Place a disclosure button near the content that it shows and hides.** Establish a clear relationship between the control and the expanded choices that appear when a person clicks or taps a button.
- **Use no more than one disclosure button in a single view.** Multiple disclosure buttons add complexity and can be confusing.

### Platform considerations
No additional considerations for macOS. Not supported in tvOS or watchOS.

#### iOS, iPadOS, visionOS
Disclosure controls are available in iOS, iPadOS, and visionOS with the SwiftUI DisclosureGroup view.

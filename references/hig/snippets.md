# Snippets
_When someone performs a task with Siri or an App Shortcut, a snippet shows the result or asks for confirmation._
Source: https://developer.apple.com/design/human-interface-guidelines/snippets

### Anatomy
  - **Dialogue.** The app intent dialogue that Siri speaks to communicate the snippet’s information. The system includes the dialogue text by default and places it above the custom view.
  - **Custom view.** A view that visually communicates the snippet’s information. A custom view can include one or more buttons for modifying the content of the snippet, getting more information, or taking another action.
  - **System-provided button(s).** A confirmation snippet includes two system-provided buttons under the custom view: a secondary Cancel button and a primary button with a customizable label. A result snippet includes a single Done button that dismisses the view.

### Best practices
- **Ensure legibility.** Check for sufficient contrast between the snippet’s custom content and the system-provided background in both light and dark appearances, and keep consistent margins for the content within the view. This clarifies the layout and helps people interpret the snippet quickly and reliably.
- **Keep content concise.** Snippets exist to facilitate lightweight, quick interactions, so it’s important to keep their content short and easily legible. To ensure all content is visible, create custom views that are no taller than the 400-point maximum height. When considering the amount of text to include, be mindful that fonts draw at various sizes based on a person’s preferred text size setting. For a result snippet, if you need to provide more detail, deep-link to the content in your app instead of including it in the custom view.
- **Choose a descriptive label for a confirmation snippet’s primary button.** You can choose an appropriate label from among those that the system provides, or you can supply a custom label. For example, when designing a snippet to order coffee, labeling the primary button Order is clearer than labeling it OK or Proceed. If you don’t specify a label, the system default is Continue.
- **Communicate a snippet’s purpose visually.** Don’t rely on showing the dialogue text to convey a snippet’s purpose. While the spoken app intent dialogue is essential for interactions when someone isn’t looking at the screen, prefer to omit it from a snippet’s visual representation and use the custom view to convey its information instead.

### Platform considerations
No additional considerations for iOS, iPadOS, or macOS. Not supported in tvOS, visionOS, or watchOS.

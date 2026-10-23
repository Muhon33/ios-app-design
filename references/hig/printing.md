# Printing
_An iOS, iPadOS, macOS, or visionOS app can integrate system-provided print functionality when it makes sense, presenting custom printer- and document-specific options if necessary._
Source: https://developer.apple.com/design/human-interface-guidelines/printing

### Best practices
- **Make printing discoverable.** Help people find your print action by placing it in standard system locations. For example, include a Print item in your macOS app’s File menu; in your iOS or iPadOS app, add a toolbar button that opens an action sheet. If your macOS app has a toolbar, you might want to put a Print button there, too, but consider making it an optional button that people can add when they customize the toolbar.
- **Present a printing option only when it’s possible.** If there’s nothing onscreen to print, or no printers are available, dim the Print item in a macOS app’s File menu and remove the Print action from the Action sheet in an iOS or iPadOS app. If you implement a custom print button, dim or hide it when printing isn’t possible.
- **Present relevant printing options.** If it makes sense to offer options like selecting a page range, requesting multiple copies, or printing on both sides — and the printer supports the options — use the system-provided view to present them.

### Platform considerations
No additional considerations for iOS, iPadOS, or visionOS. Not supported in tvOS or watchOS.

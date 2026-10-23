# File management
_Some apps can support documents and files that people expect to manage throughout the system._
Source: https://developer.apple.com/design/human-interface-guidelines/file-management

### Creating and opening files
- **Use app menus and keyboard shortcuts to give people convenient ways to create and open documents.** In iPadOS and macOS, people expect to create new documents or open existing ones using familiar menu commands. When you provide commands like New or Open, iPadOS presents them in the shortcuts interface that displays when people hold the Command key on a connected hardware keyboard, and macOS presents them in the menu bar File menu. Regardless of the availability of keyboard shortcuts, include an Add (+) button to help people create a new document. In a macOS app, you put the add action in the File menu (for guidance, see File menu).
- **If your app requires a custom file browser, support people’s understanding of the platform’s file system.** People who are familiar with the Finder and Files apps already understand the basic layout of their device’s file system. Although you might want to show the most relevant part of the file system when your custom file browser opens — for example, a Documents or iCloud folder or the most recently selected location — let people use your browser to view the rest of the file system if they want.

### Saving work
- **Help people be confident that their work is always preserved unless they cancel or delete it.** In general, avoid making people take an explicit action to save their work. Instead, automatically perform periodic saves while they’re editing and when they close a file or switch to another app.
- **Hide file extensions by default, but let people view them if they choose.** Be sure to reflect the current choice in all the save or open interfaces you display.

### Quick Look previews
- **Use a Quick Look viewer to let people preview a file even when your app can’t open it.** If your app lets people attach or otherwise interact with files that it doesn’t support, implementing a Quick Look viewer lets people preview those files without leaving your app.
- **Consider implementing a Quick Look generator if your app produces custom file types.** A Quick Look generator lets other apps — including the Finder, Files, and Spotlight — display previews of your documents, making it easier for people to find them.

### Platform considerations
No additional considerations for tvOS, visionOS, or watchOS.

#### iOS, iPadOS

##### Document launcher
Starting in iOS 18 and iPadOS 18, document-based apps can use the system’s document launcher to give people a consistent, highly graphical way to browse, open, and create files. The document launcher presents a full-screen experience that highlights key elements of your app’s theme, while making it easy for people to create new documents. For developer guidance, see DocumentGroupLaunchScene.
The document launcher consists of three main parts:
  - A title card that displays the app title and two app-specific buttons
  - A background image that appears behind the title card and additional images — called accessories — that can appear around it
  - A sheet that contains a file browser and optional app-specific controls
You can customize all three parts of the document launcher. Although the system automatically displays your app name in the title card, you specify the text and functions of the card’s primary and secondary buttons. You can also create a custom background image, one or more accessory images to surround the title card, and provide some custom controls that can appear in the file browser’s toolbar.
- **Assign the title card’s buttons to your app’s most important functions.** The primary button typically creates a new document, and the secondary button can provide additional options. For example, the primary button in Numbers is Start Writing and the secondary button is Choose a Template.
- **Provide a background that’s clearly distinct from the accessories and title card.** You can use a solid color, a gradient, or a pattern. Avoid including complex images or patterns that might distract from foreground elements.
- **Be mindful of accessory placement.** For example, you can place accessories both in front of and behind the title card to create the appearance of depth, but you need to make sure that your app name and both buttons remain clearly visible. Avoid cluttering the title card with too many accessories, and be sure to test its overall appearance across the range of screen sizes and device orientations that you support.
- **Use animation sparingly.** Too much motion on the display can confuse or disorient people. If you want to animate your accessories, consider creating gentle, repeating animations that subtly highlight and enhance your app’s content. For example, you might create an animation that makes an accessory appear to breathe or sway softly. For guidance, see Motion.

##### File provider app extension
If your app can share its files with other apps, you can create a file provider app extension that displays a custom interface for importing, exporting, opening, and moving your app’s documents. For developer guidance, see File Provider. An app extension is code you provide that people can install and use to extend the functionality of a specific area of the system; to learn more, see App extensions.
- **When someone uses your file provider extension to open or import documents, display only documents that are appropriate in the current context.** For example, if a PDF-editing app loads your extension, only list PDF files for opening or import. You might also want to display additional information, such as modification dates, sizes, and whether documents are local or remote.
- **Let people select a destination when exporting and moving documents.** Unless your app stores documents in a single directory, let people navigate to a specific destination in your directory hierarchy. You could also provide a way to add new subdirectories.
- **Avoid including a custom top toolbar.** Your extension loads within a modal view that already includes a toolbar. Providing a second toolbar is confusing and takes space away from your content.
Your app can also let people browse and open files from other apps. For developer guidance, see Adding a document browser to your app.

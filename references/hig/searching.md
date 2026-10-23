# Searching
_People use various search techniques to find content on their device, within an app, and within a document or file._
Source: https://developer.apple.com/design/human-interface-guidelines/searching

### Best practices
- **If search is important, give it a primary position in your app or view.** For example, in the Notes app, a search field is in the bottom toolbar alongside other important actions. In apps that use tab bars, like Photos and Apple TV, search is a dedicated tab.
- **Aim to make your app’s content searchable through a single location.** People appreciate having one clearly identified location they can use to find anything they’re looking for in your app. For apps with clearly distinct sections, it may still be useful to offer a local search. For example, search acts as a filter on the current view when searching your songs and albums in the iOS Music app.
- **Clearly display the current scope of a search.** Use a descriptive placeholder text, a scope bar, or a title to help reinforce what someone is currently searching. For example, in the Mail app there is always a clear reference to the mailbox someone is searching.
- **Provide suggestions to make searching easier.** When you display a personʼs recent searches before they start typing or offer predictive search suggestions while they’re typing, you can help people search faster and type less. For developer guidance, see searchSuggestions(_:).
- **Take privacy into consideration before displaying search history.** People might not appreciate having their search history appear where others might see it. If you do show search history, provide a way for people to clear it if they want.

### Systemwide search
- **Make your app’s content searchable in Spotlight.** You can share content with Spotlight by making it indexable and specifying descriptive attributes known as metadata. Spotlight extracts, stores, and organizes this information to allow for fast, comprehensive searches.
- **Define metadata for custom file types you handle.** Supply a Spotlight File Importer plug-in that describes the types of metadata your file format contains. For developer guidance, see CSImportExtension.
- **Use Spotlight to offer advanced file-search capabilities within the context of your app.** For example, you might include a button that instantly initiates a Spotlight search based on the current selection. You might then display a custom view that presents the search results or a filtered subset of them.
- **Prefer using the system-provided open and save views.** The system-provided open and save views generally include a built-in search field that people can use to search and filter the entire system. For related guidance, see File management.
- **Implement a Quick Look generator if your app produces custom file types.** A Quick Look generator helps Spotlight and other apps show previews of your documents. For developer guidance, see Quick Look.

### Platform considerations
No additional considerations for iOS, iPadOS, macOS, tvOS, visionOS, or watchOS.

# Icons
_An effective icon is a graphic asset that expresses a single concept in ways people instantly understand._
Source: https://developer.apple.com/design/human-interface-guidelines/icons

### Best practices
- **Create a recognizable, highly simplified design.** Too many details can make an interface icon confusing or unreadable. Strive for a simple, universal design that most people will recognize quickly. In general, icons work best when they use familiar visual metaphors that are directly related to the actions they initiate or content they represent.
- **Maintain visual consistency across all interface icons in your app.** Whether you use only custom icons or mix custom and system-provided ones, all interface icons in your app need to use a consistent size, level of detail, stroke thickness (or weight), and perspective. Depending on the visual weight of an icon, you may need to adjust its dimensions to ensure that it appears visually consistent with other icons.
- **In general, match the weights of interface icons and adjacent text.** Unless you want to emphasize either the icons or the text, using the same weight for both gives your content a consistent appearance and level of emphasis.
- **If necessary, add padding to a custom interface icon to achieve optical alignment.** Some icons — especially asymmetric ones — can look unbalanced when you center them geometrically instead of optically. For example, the download icon shown below has more visual weight on the bottom than on the top, which can make it look too low if it’s geometrically centered.
- **Provide a selected-state version of an interface icon only if necessary.** You don’t need to provide selected and unselected appearances for an icon that’s used in standard system components such as toolbars, tab bars, and buttons. The system updates the visual appearance of the selected state automatically.
- **Use inclusive images.** Consider how your icons can be understandable and welcoming to everyone. Prefer depicting gender-neutral human figures and avoid images that might be hard to recognize across different cultures or languages. For guidance, see Inclusion.
- **Include text in your design only when it’s essential for conveying meaning.** For example, using a character in an interface icon that represents text formatting can be the most direct way to communicate the concept. If you need to display individual characters in your icon, be sure to localize them. If you need to suggest a passage of text, design an abstract representation of it, and include a flipped version of the icon to use when the context is right-to-left. For guidance, see Right to left.
- **If you create a custom interface icon, use a vector format like PDF or SVG.** The system automatically scales a vector-based interface icon for high-resolution displays, so you don’t need to provide high-resolution versions of it. In contrast, PNG — used for app icons and other images that include effects like shading, textures, and highlighting — doesn’t support scaling, so you have to supply multiple versions for each PNG-based interface icon. Alternatively, you can create a custom SF Symbol and specify a scale that ensures the symbol’s emphasis matches adjacent text. For guidance, see SF Symbols.
- **Provide alternative text labels for custom interface icons.** Alternative text labels — or accessibility descriptions — aren’t visible, but they let VoiceOver audibly describe what’s onscreen, simplifying navigation for people with visual disabilities. For guidance, see VoiceOver.
- **Avoid using replicas of Apple hardware products.** Hardware designs tend to change frequently and can make your interface icons and other content appear dated. If you must display Apple hardware, use only the images available in Apple Design Resources or the SF Symbols that represent various Apple products.

### Standard icons

#### Editing

| Action | Icon | Symbol name |
|---|---|---|
| Cut | · | `scissors` |
| Copy | · | `document.on.document` |
| Paste | · | `document.on.clipboard` |
| Done | · | `checkmark ` |
| Save | · | · |
| Cancel | · | `xmark` |
| Close | · | · |
| Delete | · | `trash` |
| Undo | · | `arrow.uturn.backward` |
| Redo | · | `arrow.uturn.forward` |
| Compose | · | `square.and.pencil` |
| Duplicate | · | `plus.square.on.square` |
| Rename | · | `pencil` |
| Move to | · | `folder` |
| Folder | · | · |
| Attach | · | `paperclip` |
| Add | · | `plus` |
| More | · | `ellipsis` |


#### Selection

| Action | Icon | Symbol name |
|---|---|---|
| Select | · | `checkmark.circle` |
| Deselect | · | `xmark` |
| Close | · | · |
| Delete | · | `trash` |


#### Text formatting

| Action | Icon | Symbol name |
|---|---|---|
| Superscript | · | `textformat.superscript` |
| Subscript | · | `textformat.subscript` |
| Bold | · | `bold` |
| Italic | · | `italic` |
| Underline | · | `underline` |
| ​​Align Left | · | `text.alignleft` |
| Center | · | `text.aligncenter` |
| Justified | · | `text.justify` |
| Align Right | · | `text.alignright` |


#### Search

| Action | Icon | Symbol name |
|---|---|---|
| Search | · | `magnifyingglass` |
| Find | · | `text.page.badge.magnifyingglass` |
| Find and Replace | · | · |
| Find Next | · | · |
| Find Previous | · | · |
| Use Selection for Find | · | · |
| Filter | · | `line.3.horizontal.decrease` |


#### Sharing and exporting

| Action | Icon | Symbol name |
|---|---|---|
| Share | · | `square.and.arrow.up` |
| Export | · | · |
| Print | · | `printer` |


#### Users and accounts

| Action | Icon | Symbol name |
|---|---|---|
| Account | · | `person.crop.circle` |
| User | · | · |
| Profile | · | · |


#### Ratings

| Action | Icon | Symbol name |
|---|---|---|
| Dislike | · | `hand.thumbsdown` |
| Like | · | `hand.thumbsup` |


#### Layer ordering

| Action | Icon | Symbol name |
|---|---|---|
| Bring to Front | · | `square.3.layers.3d.top.filled` |
| Send to Back | · | `square.3.layers.3d.bottom.filled` |
| Bring Forward | · | `square.2.layers.3d.top.filled` |
| Send Backward | · | `square.2.layers.3d.bottom.filled` |


#### Other

| Action | Icon | Symbol name |
|---|---|---|
| Alarm | · | `alarm` |
| Archive | · | `archivebox` |
| Calendar | · | `calendar` |


### Platform considerations
No additional considerations for iOS, iPadOS, tvOS, visionOS, or watchOS.

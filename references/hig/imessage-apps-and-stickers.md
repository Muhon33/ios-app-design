# iMessage apps and stickers
_An iMessage app can help people share content, collaborate, and even play games with others in a conversation; stickers are images that people can use to decorate a conversation._
Source: https://developer.apple.com/design/human-interface-guidelines/imessage-apps-and-stickers

### Best practices
- **Prefer providing one primary experience in your iMessage app.** People are in a conversational flow when they choose your app, so your functionality or content needs to be easy to understand and immediately available. If you want to provide multiple types of functionality or different collections of content, consider creating a separate iMessage app for each one.
- **Consider surfacing content from your iOS or iPadOS app.** For example, your iMessage app could offer app-specific information that people might want to share — such as a shopping list or a trip itinerary — or support a simple, collaborative task, like deciding where to go for a meal or which movie to watch.
- **Present essential features in the compact view.** People can experience your iMessage app in a compact view that appears below the message transcript, or they can expand the view to occupy most of the window. Make sure the most frequently used items are available in the compact view, reserving additional content and features for the expanded view.
- **In general, let people edit text only in the expanded view.** The compact view occupies roughly the same space as the keyboard. To ensure that the iMessage app’s content remains visible while people edit, display the keyboard in the expanded view.
- **Create stickers that are expressive, inclusive, and versatile.** Whether your stickers are rich, static images or short animations, make sure that each one remains legible against a wide range of backgrounds and when rotated or scaled. You can also use transparency to help people visually integrate a sticker with text, photos, and other stickers.
- **For each sticker, provide a localized alternative description.** VoiceOver can help people use your sticker pack by speaking a sticker’s alternative description.

### Specifications

#### Icon sizes

| Usage | @2x (pixels) | @3x (pixels) |
|---|---|---|
| Messages, notifications | 148x110 | - |
| · | 143x100 | - |
| · | 120x90 | 180x135 |
| · | 64x48 | 96x72 |
| · | 54x40 | 81x60 |
| Settings | 58x58 | 87x87 |
| App Store | 1024x1024 | 1024x1024 |


#### Sticker sizes

| Sticker size | @3x dimensions (pixels) |
|---|---|
| Small | 300x300 |
| Regular | 408x408 |
| Large | 618x618 |


| Format | Transparency | Animation |
|---|---|---|
| PNG | 8-bit | No |
| APNG | 8-bit | Yes |
| GIF | Single-color | Yes |
| JPEG | No | No |


### Platform considerations
No additional considerations for iOS or iPadOS. Not supported in macOS, tvOS, visionOS, or watchOS.

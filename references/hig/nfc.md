# NFC
_Near-field communication (NFC) allows devices within a few centimeters of each other to exchange information wirelessly._
Source: https://developer.apple.com/design/human-interface-guidelines/nfc

### In-app tag reading
- **Don’t encourage people to make contact with physical objects.** To scan a tag, an iOS device must simply be within close proximity of the tag. It doesn’t need to actually touch the tag. Use terms like scan and hold near instead of tap and touch when asking people to scan objects.
- **Use approachable terminology.** Near-field communication may be unfamiliar to some people. To make it approachable, avoid referring to technical, developer-oriented terms like NFC, Core NFC, Near-field communication, and tag. Instead, use friendly, conversational terms that most people will understand.

| Use | Don’t use |
|---|---|
| Scan the [object name]. | Scan the NFC tag. |
| Hold your iPhone near the [object name] to learn more about it. | To use NFC scanning, tap your phone to the [object]. |

- **Provide succinct instructional text for the scanning sheet.** Provide a complete sentence, in sentence case, with ending punctuation. Identify the object to scan, and revise the text appropriately for subsequent scans. Keep the text short to avoid truncation.

| First scan | Subsequent scans |
|---|---|
| Hold your iPhone near the [object name] to learn more about it. | Now hold your iPhone near another [object name]. |


### Background tag reading
- **Support both background and in-app tag reading.** Your app must still provide an in-app way to scan tags, for people with devices that don’t support background tag reading.

### Platform considerations
No additional considerations for iOS or iPadOS. Not supported in macOS, tvOS, visionOS, or watchOS.

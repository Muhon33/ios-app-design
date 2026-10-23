# Privacy
_Privacy is paramount: it’s critical to be transparent about the privacy-related data and resources you require and essential to protect the data people allow you to access._
Source: https://developer.apple.com/design/human-interface-guidelines/privacy

### Best practices
- **Request access only to data that you actually need.** Asking for more data than a feature needs — or asking for data before a person shows interest in the feature — can make it hard for people to trust your app. Give people precise control over their data by making your permission requests as specific as possible.
- **Be transparent about how your app collects and uses people’s data.** People are less likely to be comfortable sharing data with your app if they don’t understand exactly how you plan to use it. Always respect people’s choices to use system features like Hide My Email and Mail Privacy Protection, and be sure you understand your obligations with regard to app tracking. To learn more about Apple privacy features, see Privacy; for developer guidance, see User privacy and data use.
- **Process data on the device where possible.** In iOS, for example, you can take advantage of the Apple Neural Engine and custom CreateML models to process the data right on the device, helping you avoid lengthy and potentially risky round trips to a remote server.
- **Adopt system-defined privacy protections and follow security best practices.** For example, in iOS 15 and later, you can rely on CloudKit to provide encryption and key management for additional data types, like strings, numbers, and dates.

### Requesting permission
  - Personal data, including location, health, financial, contact, and other personally identifying information
  - User-generated content like emails, messages, calendar data, contacts, gameplay information, Apple Music activity, HomeKit data, and audio, video, and photo content
  - Protected resources like Bluetooth peripherals, home automation features, Wi-Fi connections, and local networks
  - Device capabilities like camera and microphone
  - In a visionOS app running in a Full Space, ARKit data, such as hand tracking, plane estimation, image anchoring, and world tracking
  - The device’s advertising identifier, which supports app tracking
- **Request permission only when your app clearly needs access to the data or resource.** It’s natural for people to be suspicious of a request for personal information or access to a device capability, especially if there’s no obvious need for it. Ideally, wait to request permission until people actually use an app feature that requires access. For example, you can use the location button to give people a way to share their location after they indicate interest in a feature that needs that information.
- **Avoid requesting permission at launch unless the data or resource is required for your app to function.** People are less likely to be bothered by a launch-time request when it’s obvious why you’re making it. For example, people understand that a navigation app needs access to their location before they can benefit from it. Similarly, before people can play a visionOS game that lets them bounce virtual objects off walls in their surroundings, they need to permit the game to access information about their surroundings.
- **Write copy that clearly describes how your app uses the ability, data, or resource you’re requesting.** The standard alert displays your copy (called a purpose string or usage description string) after your app name and before the buttons people use to grant or deny their permission. Aim for a brief, complete sentence that’s straightforward, specific, and easy to understand. Use sentence case, avoid passive voice, and include a period at the end. For developer guidance, see Requesting access to protected resources and App Tracking Transparency.

| · | Example purpose string | Notes |
|---|---|---|
| · | The app records during the night to detect snoring sounds. | An active sentence that clearly describes how and why the app collects the data. |
| · | Microphone access is needed for a better experience. | A passive sentence that provides a vague, undefined justification. |
| · | Turn on microphone access. | An imperative sentence that doesn’t provide any justification. |


#### Pre-alert screens, windows, or views
- **Include only one button and make it clear that it opens the system alert.** People can feel manipulated when a custom screen or window also includes a button that doesn’t open the alert because the experience diverts them from making their choice. Another type of manipulation is using a term like “Allow” to title the custom screen’s button. If the custom button seems similar in meaning and visual weight to the allow button in the alert, people can be more likely to choose the alert’s allow button without meaning to. Use a term like “Continue” or “Next” to title the single button in your custom screen or window, clarifying that its action is to open the system alert.
- **Don’t include additional actions in your custom screen or window, unless needed to obtain a legal consent.** For example, don’t provide a way for people to leave the screen or window without viewing the system alert — like offering an option to close or cancel.

#### Tracking requests
- **Never precede the system-provided alert with a custom screen or window that could confuse or mislead people.** People sometimes tap quickly to dismiss alerts without reading them. A custom messaging screen, window, or view that takes advantage of such behaviors to influence choices will lead to rejection by App Store review.

### Location button
> Note: If your app has no authorization status, tapping the location button has the same effect as when a person chooses Allow Once in the standard alert. If people previously chose While Using the App, tapping the location button doesn’t change your app’s status. For developer guidance, see LocationButton (SwiftUI) and CLLocationButton (Swift).
- **Consider using the location button to give people a lightweight way to share their location for specific app features.** For example, your app might help people attach their location to a message or post, find a store, or identify a building, plant, or animal they’ve encountered in their location. If you know that people often grant your app Allow Once permission, consider using the location button to help them benefit from sharing their location without having to repeatedly interact with the alert.
- **Consider customizing the location button to harmonize with your UI.** Specifically, you can:
  - Choose the system-provided title that works best with your feature, such as “Current Location” or “Share My Current Location.”
  - Choose the filled or outlined location glyph.
  - Select a background color and a color for the title and glyph.
  - Adjust the button’s corner radius.
> Important: If the system identifies consistent problems with your customized location button, it won’t give your app access to the device location when people tap it. Although such a button can perform other app-specific actions, people may lose trust in your app if your location button doesn’t work as they expect.

### Protecting data
- **Avoid relying solely on passwords for authentication.** Where possible, use passkeys to replace passwords. If you need to continue using passwords for authentication, augment security by requiring two-factor authentication (for developer guidance, see Securing Logins with iCloud Keychain Verification Codes). To further protect access to apps that people keep logged in on their device, use biometric identification like Face ID, Optic ID, or Touch ID. For developer guidance, see Local Authentication.
- **Store sensitive information in a keychain.** A keychain provides a secure, predictable user experience when handling someone’s private information. For developer guidance, see Keychain services.
- **Never store passwords or other secure content in plain-text files.** Even if you restrict access using file permissions, sensitive information is much safer in an encrypted keychain.
- **Avoid inventing custom authentication schemes.** If your app requires authentication, prefer system-provided features like passkeys, Sign in with Apple or Password AutoFill. For related guidance, see Managing accounts.

### Platform considerations
No additional considerations for iOS, iPadOS, tvOS, or watchOS.

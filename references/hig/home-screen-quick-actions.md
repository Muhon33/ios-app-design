# Home Screen quick actions
_Home Screen quick actions give people a way to perform app-specific actions from the Home Screen._
Source: https://developer.apple.com/design/human-interface-guidelines/home-screen-quick-actions

### Best practices
- **Create quick actions for compelling, high-value tasks.** For example, Maps lets people search near their current location or get directions home without first opening the Maps app. People tend to expect every app to provide at least one useful quick action; you can provide a total of four.
- **Avoid making unpredictable changes to quick actions.** Dynamic quick actions are a great way to keep actions relevant. For example, it may make sense to update quick actions based on the current location or recent activities in your app, time of day, or changes in settings. Make sure that actions change in ways that people can predict.
- **For each quick action, provide a succinct title that instantly communicates the results of the action.** For example, titles like “Directions Home,” “Create New Contact,” and “New Message” can help people understand what happens when they choose the action. If you need to give more context, provide a subtitle too. Mail uses subtitles to indicate whether there are unread messages in the Inbox and VIP folder. Don’t include your app name or any extraneous information in the title or subtitle, keep the text short to avoid truncation, and take localization into account as you write the text.
- **Provide a familiar interface icon for each quick action.** Prefer using SF Symbols to represent actions. For a list of icons that represent common actions, see Standard icons; for additional guidance, see Menus.
- **Don’t use an emoji in place of a symbol or interface icon.** Emojis are full color, whereas quick action symbols are monochromatic and change appearance in Dark Mode to maintain contrast.

### Platform considerations
No additional considerations for iOS or iPadOS. Not supported in macOS, tvOS, visionOS, or watchOS.

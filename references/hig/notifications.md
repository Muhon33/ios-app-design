# Notifications
_A notification gives people timely, high-value information they can understand at a glance._
Source: https://developer.apple.com/design/human-interface-guidelines/notifications

### Anatomy
  - A banner or view on a Lock Screen, Home Screen, Home View, or desktop
  - A badge on an app icon
  - An item in Notification Center

### Best practices
- **Provide concise, informative notifications.** People turn on notifications to get quick updates, so you want to provide valuable information succinctly.
- **Avoid sending multiple notifications for the same thing, even if someone hasn’t responded.** People attend to notifications at their convenience. If you send multiple notifications for the same thing, you fill up Notification Center, and people may turn off all notifications from your app.
- **Avoid sending a notification that tells people to perform specific tasks within your app.** If it makes sense to offer simple tasks that people can perform without opening your app, you can provide notification actions. Otherwise, avoid telling people what to do because it’s hard for people to remember such instructions after they dismiss the notification.
- **Use an alert — not a notification — to display an error message.** People are familiar with both alerts and notifications, so you don’t want to cause confusion by using the wrong component. For guidance, see Alerts.
- **Handle notifications gracefully when your app is in the foreground.** Your app’s notifications don’t appear when your app is in the front, but your app still receives the information. In this scenario, present the information in a way that’s discoverable but not distracting or invasive, such as incrementing a badge or subtly inserting new data into the current view. For example, when a new message arrives in a mailbox that people are currently viewing, Mail simply adds it to the list of unread messages because sending a notification about it would be unnecessary and distracting.
- **Avoid including sensitive, personal, or confidential information in a notification.** You can’t predict what people will be doing when they receive a notification, so it’s essential to avoid including private information that could be visible to others.

### Content
- **Create a short title if it provides context for the notification content.** Prefer brief titles that people can read at a glance, especially on Apple Watch, where space is limited. When possible, take advantage of the prominent notification title area to provide useful information, like a headline, event name, or email subject. If you can only provide a generic title for a noncommunication notification — like New Document — it can be better to let the system display your app name instead. Use title-style capitalization and no ending punctuation.
- **Write succinct, easy-to-read notification content.** Use complete sentences, sentence case, and proper punctuation, and don’t truncate your message — the system does this automatically when necessary.
- **Provide generically descriptive text to display when notification previews aren’t available.** In Settings, people can choose to hide notification previews for all apps. In this situation, the system shows only your app icon and the default title Notification. To give people sufficient context to know whether they want to view the full notification, write body text that succinctly describes the notification content without revealing too many details, like “Friend request,” “New comment,” “Reminder,” or “Shipment” (for developer guidance, see hiddenPreviewsBodyPlaceholder). Use sentence-style capitalization for this text.
- **Avoid including your app name or icon.** The system automatically displays a large version of your app icon at the leading edge of each notification; in a communication notification, the system displays the sender’s contact image badged with a small version of your icon.
- **Consider providing a sound to supplement your notifications.** Sound can be a great way to distinguish your app’s notifications and get someone’s attention when they’re not looking at the device. You can create a custom sound that coordinates with the style of your app or use a system-provided alert sound. If you use a custom sound, make sure it’s short, distinctive, and professionally produced. A notification sound can enhance the user experience, but don’t rely on it to communicate important information, because people may not hear it. Although people might also want a vibration to accompany alert sounds, you can’t provide such a vibration programmatically. For developer guidance, see UNNotificationSound.

### Notification actions
- **Provide beneficial actions that make sense in the context of your notification.** Prefer actions that let people perform common, time-saving tasks that eliminate the need to open your app. For each button, use a short, title-case term or phrase that clearly describes the result of the action. Don’t include your app name or any extraneous information in the button label, keep the text brief to avoid truncation, and take localization into account as you write it.
- **Avoid providing an action that merely opens your app.** When people tap a notification or its preview, they expect your app to display related content, so presenting an action button that does the same thing clutters the detail view and can be confusing.
- **Prefer nondestructive actions.** If you must provide a destructive action, make sure people have enough context to avoid unintended consequences. The system gives a distinct appearance to the actions you identify as destructive.
- **Provide a simple, recognizable interface icon for each notification action.** An interface icon reinforces an action’s meaning, helping people instantly understand what it does. The system displays your interface icon on the trailing side of the action title. When you use SF Symbols, you can choose an existing symbol that represents your command or edit a related symbol to create a custom icon.

### Badging
- **Use a badge only to show people how many unread notifications they have.** Don’t use a badge to convey numeric information that isn’t related to notifications, such as weather-related data, dates and times, stock prices, or game scores.
- **Make sure badging isn’t the only method you use to communicate essential information.** People can turn off badging for your app, so if you rely on it to show people when there’s important information, people can miss the message. Always make sure that you make important information easy for people to find as soon as they open your app.
- **Keep badges up to date.** Update your app’s badge as soon as people open the corresponding notifications. You don’t want people to think there are new notifications available, only to find that they’ve already viewed them all. Note that reducing a badge’s count to zero removes all related notifications from Notification Center.
- **Avoid creating a custom image or component that mimics the appearance or behavior of a badge.** People can turn off notification badges if they choose, and will become frustrated if they have done so and then see what appears to be a badge.

### Platform considerations
No additional considerations for iOS, iPadOS, macOS, tvOS, or visionOS.

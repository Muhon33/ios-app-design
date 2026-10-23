# CareKit
_People can use CareKit apps to manage care plans related to a chronic illness like diabetes, recover from an injury or surgery, or achieve health and wellness goals._
Source: https://developer.apple.com/design/human-interface-guidelines/carekit

### Data and privacy
- **Provide a coherent privacy policy.** During the app submission process, you must provide a URL to a clearly stated privacy policy, so that people can view the policy when they click the link in the App Store page for your app. For developer guidance, see App information > App Store Connect help.

#### HealthKit integration
- **Request access to health data only when you need it.** It makes sense to request access to weight information when people log their weight, for example, but not immediately after your app launches. When your request is clearly related to the current context, you help people understand your app’s intentions. Also, people can change the permissions they grant, so it’s a good idea to make a request every time your app needs access. For developer guidance, see requestAuthorization(toShare:read:completion:).
- **Clarify your app’s intent by adding descriptive messages to the standard permission screen.** People expect to see the system-provided permission screen when asked to approve access to health data. Write a few succinct sentences that explain why you need the information and how people can benefit from sharing it with your app. Avoid adding custom screens that replicate the standard permission screen’s behavior or content.
- **Manage health data sharing solely through the system’s privacy settings.** People expect to globally manage access to their health information in Settings > Privacy. Don’t confuse people by building additional screens in your app that affect the flow of health data.

#### Motion data

#### Photos

#### ResearchKit integration

### CareKit views

| Category | Purpose |
|---|---|
| Tasks | Present tasks, like taking medication or doing physical therapy. Support logging of patient symptoms and other data. |
| Charts | Display graphical data that can help people understand how their treatment is progressing. |
| Contact views | Display contact information. Support communication through phone, message, and email, and link to a map of the contact’s location. |


#### Tasks

| Information | Required | Description | Example value |
|---|---|---|---|
| Title | Yes | A word or short phrase that introduces the task. | Ibuprofen |
| Schedule | Yes | The schedule on which a task must be completed. | Four times a day |
| Instructions | No | Detailed instructions, recommendations, and warnings. | Take 1 tablet every 4–6 hours (not to exceed 4 tablets daily). |
| Group ID | No | An identifier you can use to group similar tasks in ways that make sense in your app. | A category identifier like medication or exercise. |

- **Use the simple style for a one-step task.** The default simple-style view consists of a header area that contains a title, subtitle, and button. You provide the title and subtitle, and you can provide a custom image to display in the button when the task is complete. If you don’t supply an image, CareKit shows that a task is complete by filling in the button and displaying a checkmark. Because the default simple-style view doesn’t include a content stack, consider using a different task style if you need to display additional content.
- **Use the instructions style when you need to add informative text to a simple task.** For example, if a single-step medication task needs to include additional information — such as “Take on an empty stomach” or “Take at bedtime” — you can use an instructions-style task to display it.
- **Use the log style to help people log events.** For example, you could use this task style to display a button people can tap whenever they feel nauseated. The log-style task can automatically display a timestamp every time the patient logs an event.
- **Use the checklist style to display a list of actions or steps in a multistep task.** For example, if people must take a medication three times per day, you could display the three scheduled times in a checklist. Each checklist item can include a text description and a button that people can tap to mark the item as done. By default, a checklist task can also display instructional text below the list.
- **Use the grid style to display a grid of buttons in a multistep task.** Like the checklist style, the grid style also supports a multistep task, but it displays the steps in a more compact arrangement. You can supply a succinct title for each button (if you need to provide additional description for each button, you might want to use the checklist style instead). By default, a grid-style task can also display instructional text below the grid of buttons. Unlike other task styles, the grid style gives you access to its underlying collection view, which means that you can display custom UI elements in the grid layout.
- **Consider using color to reinforce the meaning of task items.** Color can be a good way to help people understand information at a glance. For example, you could use one color for medications and a different color for physical activities. Always avoid using color as the only way to convey information. For guidance, see Color.
- **Combine accuracy with simplicity when describing a task and its steps.** For example, use a medication’s marketing name instead of its chemical description. Also, when the context of a task helps to clarify meaning, minimize the number of words you use. For example, a daily medication task generally tells people when to take specific medications, so it may be unnecessary to repeat words like take.
- **Consider supplementing multistep or complex tasks with videos or images.** Visually demonstrating how to perform a task can help people avoid mistakes.

#### Charts
- **Consider highlighting narratives and trends to illustrate progress.** For example, your app could display a bar chart that shows a correlation between the number of times people took medication and their level of pain. Displaying such data can encourage better adherence to a care plan.
- **Label chart elements clearly and succinctly.** Long, detailed labels can make a chart difficult to read and understand. Keep labels short and avoid repeating the same information. For example, a heart rate chart might use the term BPM in an axis label instead of using it in the label of every data point.
- **Use distinct colors.** In general, avoid using different shades of the same color to mean different things. Also ensure that you use colors with sufficient contrast. For related guidance, see Accessibility.
- **Consider providing a legend to add clarity.** If the colors you use to represent different types of data aren’t immediately clear, include a legend that clearly and succinctly describes them.
- **Clearly denote units of time.** People need to know whether time-based data is represented in seconds, minutes, hours, days, weeks, months, or years. If you don’t want to include this information in individual data value labels, include it in an axis label or elsewhere on the chart.
- **Consolidate large data sets for greater readability.** A large amount of data can make a chart unreadable by reducing the size of individual data points and presenting too much visible information. Look for ways to group and organize data for clarity and simplicity.
- **If necessary, offset data to keep charts proportional.** It’s easy for very small data points to get lost or become unreadable in a chart that also contains very large data points. If the difference between data points is significant, find ways to offset or restructure the data so all data points are readable.

#### Contact views
- **Consider using color to categorize care team members.** Color can help people identify care team members at a glance.

### Notifications
- **Minimize notifications.** Care plans vary from patient to patient. While one individual may have only a few daily tasks to complete, another may have a long list. Use notifications sparingly so people don’t feel overwhelmed. When possible, consider coalescing multiple items into a single notification.
- **Consider providing a detail view.** In addition to providing more information, a notification detail view can help people take immediate action without leaving their current context to open your app. For example, you could use a notification detail view to display a list of pending tasks so that people can quickly mark them as complete.

### Symbols and branding
  - Designs that coordinate with CareKit’s visual design language
  - Support for creating custom symbols to represent the unique content in your app
- **Design a relevant care symbol.** If you need to customize a symbol, be sure the design is closely related to your app or the general concept of health and wellness. Avoid creating a purely decorative symbol or using a corporate logo as a custom symbol.
- **Incorporate refined, unobtrusive branding.** People use CareKit apps to help them achieve their health and wellness goals; they don’t want to see advertising. To avoid distracting people from their care plan, subtly incorporate your brand through your app’s use of color and communication style.

### Platform considerations
No additional considerations for iOS or iPadOS. Not supported in macOS, tvOS, visionOS, or watchOS.

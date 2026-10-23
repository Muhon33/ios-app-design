# Siri
_People use Siri to help them with the things they need to find, know, or do every day._
Source: https://developer.apple.com/design/human-interface-guidelines/siri

### Getting your app to work with Siri

#### Sharing contextual information

### Best practices
- **Identify your app’s most popular actions, and when and where they occur.** Understanding the contexts where those actions are relevant, such as in a hands-free environment or on a particular device, can help you prioritize which actions and content to expose as app intents and entities, and inform how you design a great Siri experience.
- **Use familiar terms for your content and actions.** When you create an app intent or entity, you choose the terminology that represents it. For example, you could refer to an audio file as a track, a song, or a podcast. Using language for your features and content that people are most likely to recognize makes interacting with your app through Siri more natural and intuitive.
- **Offer relevant content.** Instead of telling Spotlight about all of your app’s content, consider things that are particularly relevant to someone’s personal context — things they’ve recently searched for, their favorite items or bookmarks, or the content of a wishlist. Some app categories, like email or messaging, might have a good reason to consider their entire catalog as relevant information; it can be appropriate to provide expanded access in those cases.
- **Don’t advertise.** Don’t include advertisements, marketing, or in-app purchase sales pitches in content that Siri delivers.
- **Only provide a custom response if built-in responses don’t meet your app’s needs.** Siri is designed to anticipate a wide variety of natural language requests and respond helpfully without additional configuration.

### Customizing your app’s experience with Siri
> Note: Siri is powered by Apple Intelligence to provide contextually relevant responses. Because responses can appear in a wide variety of contexts, some of which aren’t visual, optional intent or entity properties that an app defines may not always appear as part of a response.
- **Write response dialogue that’s clear and descriptive.** An effective response clearly conveys what happens when Siri performs the action. If you ask follow-up questions, be sure to customize the default dialogue for clarity. For example, “Which soup?” is clearer than “Which one?”
- **Keep responses as succinct as possible.** People might interact with Siri frequently, so they may hear the same response multiple times when answering follow-up questions or dealing with errors. Use the context of the current conversation to remove as many details as possible. Avoid including unnecessary words or attempts at humor, because both can become irritating over time.
- **Provide responses that Siri can deliver audibly and visually.** This lets Siri decide which communication method works best for the current situation. For example, if someone using iPhone asks for the weather, the forecast appears onscreen; if they’re using AirPods, Siri speaks the forecast instead. Make sure the voice response can stand alone and that it doesn’t depend on visual elements to fill in essential information.
- **Design inclusive interactions.** Create welcoming interactions for everyone by avoiding specific pronouns when they’re not necessary. For example, in response to “Send a message to my best friend,” instead of saying “What’s his or her name?” say “Who should I send it to?” or “To who?” For guidance, see Writing and Inclusion.
- **Ask an open-ended question when the full list of options is too long.** If the full list of options is too long for Siri to read in a timely way, follow up with an open-ended question to narrow the scope or get additional detail. For example, “What kind of shoes are you interested in?” in response to a request for the available shoes in a shopping app.
- **Keep responses device-independent whenever possible.** People can initiate a Siri request on one device and have it take effect on another, so device-specific wording can easily become confusing or misleading. If you must reference a specific device in a response, make sure it’s accurate and makes sense in context.
- **Omit your app name from responses.** The system already provides verbal and visual attribution for your app when responding to people.
- **Use appropriate language and respect parental controls.** Don’t include offensive language in dialogue text that you provide. Many families use parental controls to restrict explicit content and other material that’s based on specific rating levels. Be aware that Siri may also respond aloud, and others nearby might hear the response.
- **Help people understand errors and failures.** The system provides some default error descriptions, but it’s best to enhance error responses so that they’re specific to the current situation. For example, if the chicken noodle soup is sold out, an error like “Sorry, we’re out of chicken noodle soup” is much clearer than “Sorry, we can’t complete your order.”

### Editorial guidelines
- **Refer to Siri by name.** Don’t reference Siri using pronouns like she, him, or her. Ideally, just use the word Siri. For example, “After you add a shortcut to Siri, you can run the shortcut anytime by asking Siri.” For additional guidance, see Guidelines for Using Apple Trademarks.
- **Be aware that the system reserves important actions and phrases for Siri.** Never impersonate Siri, attempt to reproduce the functionality that Siri provides, or provide a response that appears to come from Apple. Don’t use reserved phrases like “Call 911” or “Hey Siri.”
- **In a localized context, translate only the word Hey in the phrase “Hey Siri.”** As an Apple trademark, Siri is never translated. Here is a list of acceptable translations for the phrase “Hey Siri”:

| Locale code | “Hey Siri” translation | Locale code | “Hey Siri” translation |
|---|---|---|---|
| ar_AE | يا Siri | fr_CA | Dis Siri |
| ar_SA | يا Siri | fr_CH | Dis Siri |
| da_DK | Hej Siri | fr_FR | Dis Siri |
| de_AT | Hey Siri | it_CH | Ehi Siri |
| de_CH | Hey Siri | it_IT | Ehi Siri |
| de_DE | Hey Siri | ja_JP | Hey Siri |
| en_AU | Hey Siri | ko_KR | Siri야 |
| en_CA | Hey Siri | ms_MY | Hai Siri |
| en_GB | Hey Siri | nb_NO | Hei Siri |
| en_IE | Hey Siri | nl_BE | Hé, Siri |
| en_IN | Hey Siri | nl_NL | Hé Siri |
| en_NZ | Hey Siri | no_NO | Hei Siri |
| en_SG | Hey Siri | pt_BR | E aí Siri |
| en_US | Hey Siri | ru_RU | привет Siri |
| en_ZA | Hey Siri | sv_SE | Hej Siri |
| es_CL | Oye Siri | th_TH | หวัดดี Siri |
| es_ES | Oye Siri | tr_TR | Hey Siri |
| es_MX | Oye Siri | zh_CN | 嘿Siri |
| es_US | Oye Siri | zh_HK | 喂 Siri |
| fi_FI | Hei Siri | zh_TW | 嘿 Siri |
| fr_BE | Dis Siri | · | · |

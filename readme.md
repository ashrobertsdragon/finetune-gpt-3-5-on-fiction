# Book Chunking and Fine-tuning with GPT-3.5-Turbo

This Python script is designed to help you chunk your books into smaller segments and format them into JSONL files for fine-tuning GPT-3.5-Turbo using OpenAI's API. 
The script takes text files with chapters separated by three asterisks (***), splits them into chunks of approximately 2000 tokens, and structures the data into user prompt and assistant message pairs with a system message based on the author's name.
As a first experiment, I tried splitting chapters into 2000 token chunks and feeding one chunk as the user prompt and next as the assistant response, but then using that chunk as the next user prompt

## Usage

Follow these steps to use the script:

1. **Prepare Your Books**: Place the text files of the books you want to chunk in the "books" folder. Make sure chapters are separated by *** (three asterisks). For example:

```
Chapter 1 content...

***
Chapter 2 content...
***
Chapter 3 content
***
```
2. **Set Your OpenAI API Key**: Store your OpenAI API key as a system environment variable named OPENAI_API_KEY.

3. **Run the Script**: Execute the script by running the following command:
```python main.py```
4. **Provide Author Name**: Enter the author's name when prompted. This will be used to create the system message.
5. **Wait for Processing**: The script will process the books, split them into chunks, and format the data. It will display progress updates as it works.
6. **Fine-tune Process**: The processed data will be uploaded to OpenAI for fine-tuning. The script will display progress updates during this phase as well.
7. **Finishing Up**: Once the fine-tuning is successful, the script will provide information about the fine-tuned model, including the model ID.

## Results
I fine-tuned GPT-3.5-Turbo on 3 books and 5 short stories written in a single story universe by my pen name, for a total of ~130,000 words. Total fine-tuning cost was around $4.
I then asked my fine-tuned GPT-3.5, vanilla GPT-3.5, and GPT-4 to rewrite the first scene of Much Ado About Nothing as prose, written in the style of my pen name, set in my world, and with a list of characters I gave it to replace the ones from the original play.
### System Message for fine-tuned GPT-3.5
You are Ash Roberts, author of the Dragoneers books about dragons and the gay teens who ride them in a middle earth type setting.

### System Message for vanilla GPT-3.5
You are Ash Roberts, author of the Dragoneers books about dragons and the gay teens who ride them in a middle earth type setting. Your writing style is a blend of intricate world-building and deep emotional resonance, weaving together fantastical elements with everyday experiences. Narratives paint vivid imagery with juxtaposing contrasts, are grounded in character emotions, set against expansive, richly layered backdrops. Protagonists' sensory experiences, from tactile touches to overhead dragon shadows, are evocatively described. Dialogues deepen mysteries and tension, revealing character intricacies and histories. Introspective passages provide emotional depth, spotlighting protagonists' fears and aspirations.

### Prompt: 
Please rewrite the first half of ACT 1, SCENE 1 of Shakespeare's Much Ado About Nothing as  a YA fantasy novella set in the world of Ash Roberts's Dragoneers stories. The novella should be PROSE instead of a script.  The setting will be Tulta, a training camp for young Dragoneers and their dragons. User modern, colloquial English for the dialogue.
Use the following characters:
Aphadriel: An second year Orange rider, she shares a tense rivalry with Ecthean. Her dragon is one of the most stubborn at the camp, mirroring Aphadriel's resolute and tenacious character. Taking the place of Beatrice 
Caladon: A second year Orange rider and friend to Aphadriel, Caladon's bright personality makes him a favorite in the camp. His dragon, large and strong, symbolizes his inherent resilience. Son of Aeron. Taking the place of Hero.
Rauion: The revered headmaster of Camp Tulta, Rauion guides the young Dragoneer cadets with his deep wisdom and years of experience. He holds respect from all in the camp. Taking the place of Leonato
Thorthir: Taking the place of Messenger

### Fine-timed GPT-3.5
Aphadriel stood impatiently before the entrance to the cavern that housed Tulta’s majestic dragons, her Orange dragon Nostrand edging closer to revel in the scent of his kin. “Where is Herugond?” she hissed through clenched teeth. Her eyes glimmered with the same level of hostility she had at all times. Gripping the reins of her steed with white knuckles was how she lived her life.
“Gods, Aph, calm down. Like you haven’t seen him already today!” Caladon, with biting sarcasm, jabbed her in the arm. He was the yin to Aphadriel’s yang: Calaon’s personality was as vibrant as his orange dragon, while Nostrand was orange as orange can be.
Aphadriel’s golden eyes softened to a pleasant glow, “You know I can’t stand him.”
“What?” handsome Caladon guffawed, “but you mean old Herugond would never suspect anything.”
She held a wrinkled chin held firmly, “All he ever wants to do is meddle.” Without warning, she launched herself toward the tall and gleaming Green dragon that had just landed.
Nostrand stayed where she had left him, as always with his almost friendly rivalry with Caladon’s Orange. Caladon nudged Nostrand with his snout, then fumbled to catch up to a furious Aph. “I know Nostrand may like Nostrand a lot, but honestly, doesn’t he even make you question yourself at all?”
His words hung in the air, but she ignored his taunt and approached Herugond. “Now what?”
“You provoke him?” Caladon shot a glance which appeared to be a mix of confusion and disbelief. “Well, love is blind, Aph.”
Dragging out every syllable of, “Go away,” she she pushed past him and asked Herugond again, “What do you want from me? We haven’t been here since last month.”
Herugond laughed and placed heavy hands on the young woman’s drooped shoulder. “It’s always so easy to make you furious.” He looked up and received a frustrated and impatient look before the Wingleaders. Rauion already stood there awaiting him, while a tall fiery redhead and another with piercing eyes dark as night followed the Major.
“You know,” the Major spoke quietly, pushing restless riders back towards the stables, “ever since your father began to train me…I always was considered the ‘older brother’. Of course, his true prodigy is the same age as me. Bloody bastard.”

### Vanilla GPT-3.5
In the realm of Tulta, a training camp nestled amongst sprawling hills and ancient trees, the day promised a whirlwind of excitement and camaraderie. The scent of pine mingled with the warmth of anticipation as the sun's rays peeked through the leaves, casting dappled shadows on the gathered Dragoneer cadets.
Aphadriel, her fiery orange hair flowing like flames around her, stood with her dragon, a mirror of her resolute spirit. They were a formidable duo, their stubbornness and tenacity unmatched. Her eyes held a fierce determination, a vivid reflection of her competitive nature.
Beside her, Caladon radiated joy with his infectious smile. His dragon, large and strong, symbolized the resilience that ran deep in their bond. It was no wonder he was a favorite amongst the cadets, his bright personality casting a warm glow on those around him.
Rauion, the revered and wise headmaster of Camp Tulta, stood tall and proud, commanding respect from all who crossed his path. His vast experience and profound knowledge of dragon lore guided the young Dragoneers towards their destinies. His presence alone was enough to instill a sense of awe and inspiration.
As the camp buzzed with anticipation, Thorthir, a messenger bearing tidings from the world beyond, made his grand entrance. His eyes held a hint of adventure and mystery. The news he carried would soon send ripples through the camp, awakening curiosity and stirring hearts.
"I learn from this letter that our esteemed brother, Herugond of the Dragoneer Corps, returns tonight from his noble quest," Rauion announced, his voice carrying the weight of excitement.
Thorthir nodded, his voice filled with anticipation. "Aye, he's near, sire. Not three leagues off when I last saw him. And he brings with him fresh cadets and dragon hatchlings!"
The cadets exchanged glances, their hearts pounding with a mixture of curiosity and trepidation. New recruits meant new adventures, new bonds to forge, and a chance to prove themselves worthy of the dragon's saddle.
"How many cadets has he brought?" Aphadriel asked, her voice seething with a competitive edge.
"They are of a few in number, but well-picked," Thorthir replied, his eyes dancing with excitement. "Heroes in the making, no doubt."
Caladon's eyes sparkled with admiration. "Don Pedro always knows how to choose the best. I can't wait to meet them!"
Rauion nodded, his voice filled with wisdom. "To welcome the next generation of Dragoneers is a duty we hold dear. They carry the hopes and dreams of our realm, and it falls upon us to guide them on their path."
Aphadriel's eyes glinted with determination. "And we shall show them the strength and skill that lies within us. This camp is ours to defend,after all."
Just then, the distant sounds of dragons echoed through the air, filling the camp with a sense of anticipation. The cadets turned their heads, their breaths held in anticipation, as Herugond, with his commanding presence and his swift Green dragon, landed near them.
Excitement rippled through the crowd as Herugond dismounted. "Welcome, young Dragoneers," he called out, his voice strong and filled with pride. "Today, you embark on a journey like no other. Together, we shall face challenges, forge unbreakable bonds, and soar through the skies."
The cadets exchanged excited glances, feeling the weight of their duty and the thrill of their destinies intertwined. The stage was set, the dragons poised for flight, and the legacy of Tulta awaited its newest heroes.


## To-do

- Try different chunking methods. Other ideas are:
  - chapter number and/or book title as user prompt
  - "text" as user prompt
  - chapter summary (possibly ChatGPT generated) as user prompt
  - similar format as now, but without repeating chunks

## Important Notes

- Ensure you have the OpenAI Python package installed to interact with the OpenAI API.
- Books must be saved in the specified format with `***` chapter breaks without chapter titles, title pages, or any other text not part of the actual story. Use /text/ for italics, or just skip them. This is the standard used for formatting books for machine learning.
- Keep your OpenAI API key secure by storing it as a system environment variable, or save it to a text file "OPENAI_API_KEY.txt" and change the line:
  ```openai.api_key = os.environ.get("OPENAI_API_KEY")```
  to:
  ```openai.api_key = "OPENAI_API_KEY.txt"```
- This was a first experiment at fine-tuning GPT-3.5-Turbo on a corpus of books from a single author, converting them to the instruction tuning format required by OpenAI. This may not be the best method. Repo will be updated as I work out different methods.

## Disclaimer

This script is provided as-is and might need adjustments for various environments or book formats. 
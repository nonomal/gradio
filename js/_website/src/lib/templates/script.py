

content = """
<script lang="ts">
    import {{get_object}} from "./process_json.ts";
    import ParamTable from "../ParamTable.svelte";
    import ShortcutTable from "../ShortcutTable.svelte";
    import DemosSection from "../DemosSection.svelte";
    import FunctionsSection from "../FunctionsSection.svelte";
    import GuidesSection from "../GuidesSection.svelte";


    let obj = get_object("{}");
</script>

<!--- Title -->
# {{obj.name}}

<!--- Usage and Embedded Component -->
<div class="codeblock"><pre><code class="code language-python">{{obj.parent}}.{{obj.name}}(···)</code></pre></div>
<div class="embedded-component mt-3"><gradio-app space={{"gradio/" + obj.name.toLowerCase() + "_component"}}/></div>

<!--- Description -->
### Description
## {{obj.description}}

<!--- Behavior -->
### Behavior
## **As input component**: {{obj.preprocess.return_doc.doc}}
## **As output component**: {{obj.postprocess.parameter_doc[0].doc}}

<!--- Initialization -->
### Initialization
<ParamTable parameters={{obj.parameters}} />

<!--- Shortcuts -->
### Shortcuts
<ShortcutTable shortcuts={{obj.string_shortcuts}} />

<!--- Demos -->
### Demos 
<DemosSection demos={{obj.demos}} />

<!--- Event Listeners -->
### Event Listeners 
<FunctionsSection fns={{obj.fns}} event_listeners={{true}} />

<!--- Guides -->
### Guides
<GuidesSection guides={{obj.guides}}/>
"""


import json

PATH = "./gradio/"

with open("../json/docs.json", "r") as j:
    data = json.load(j)


components = list(data["docs"]["components"].keys())


for component in components:
    with open(PATH + f"{component}.svx", "w+") as file:
        file.write(content.format(component))
    print(f"Created {component}.svx")
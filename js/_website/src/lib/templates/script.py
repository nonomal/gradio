

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

<!--- Usage -->
<div class="codeblock"><pre><code class="code language-python">{{obj.parent}}.{{obj.name}}(···)</code></pre></div>

<!--- Description -->
### Description
## {{obj.description}}

<!-- Behavior -->
### Behavior
## **As input component**: {{obj.preprocess.return_doc.doc}}
##### Your function should accept one of these types:

## **As output component**: {{obj.postprocess.parameter_doc[0].doc}}
##### Your function should return one of these types:



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

{{#if obj.guides && obj.guides.length > 0}}
<!--- Guides -->
### Guides
<GuidesSection guides={{obj.guides}}/>
{{/if}}
"""


import json

PATH = "./gradio/"

with open("../json/docs.json", "r") as j:
    data = json.load(j)

print(data["docs"]["components"].keys())
components = [component for component in data["docs"]["components"].keys()]

for component in components:
    with open(PATH + f"{component}.svx", "w+") as file:
        file.write(content.format(component))
    print(f"Created {component}.svx")
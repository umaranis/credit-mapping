<script lang="ts">
    import type { PageData } from './$types';
    export let data: PageData;

    import { getContext } from 'svelte';
	import type { Writable } from 'svelte/store';

	const currentPage = getContext<Writable<string>>('currentPage');
	$currentPage = 'compare';

    let full: string = "";
    for(let i=0;i<data.courseDesc.length;i++){
        full += data.courseDesc[i].content + "\n\n";
    }
    


</script>

<h1>THIS PAGE THIS PAGE THIS PAGE</h1>

<h1>View Course</h1>
<label>Unit ID: {data.unitid}</label>


<div style="margin:20px auto; width:90%;">
    <div style="width:45%;display:inline-block">
        <textarea id="sentence1" name="sentence1" style="width:100%;height:700px;color:black;">
            {full}
        </textarea>
        
    </div>
    <div style="width:45%;height:700px; display:inline-block;color:black;">
        <textarea id="sentence2" name="sentence2" style="width:100%;height:700px;"></textarea>
    </div>
    
</div>

<div style="padding-bottom: 10px;">
    <a><label style="border: 1px solid; border-radius: 10px; width: 300px;text-align: center;margin:0 auto;">Compare Courses</label></a>
</div>

<style>
    h1 {
        text-align: center;
        font-size: 2em;
        padding-bottom: 10px;
    }

    label {
        padding: 10px;
    }
</style>
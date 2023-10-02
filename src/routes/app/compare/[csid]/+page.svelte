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

<h1>View Course</h1>
<label>Unit ID: {data.unitid}</label>


<div style="margin:20px auto; width:90%;">
    <div style="width:45%;display:inline-block">
        <textarea id="sentence1" name="sentence1" style="width:100%;height:700px;color:black;">
            {full}
        </textarea>
        <div id="wordCount1">Word count: 0</div>
        <script>
            document.addEventListener('DOMContentLoaded', function () {
                var textArea1 = document.getElementById('sentence1');
                var wordCountDisplay1 = document.getElementById('wordCount1');

                var textArea2 = document.getElementById('sentence2');
                var wordCountDisplay2 = document.getElementById('wordCount2');
    
                textArea1.addEventListener('input', function () {
                    var text = textArea1.value;
                    var wordCount1 = countWords(text);
                    wordCountDisplay1.textContent = 'Word count: ' + wordCount1 + ' /384';
                });

                textArea2.addEventListener('input', function () {
                    var text = textArea2.value;
                    var wordCount2 = countWords(text);
                    wordCountDisplay2.textContent = 'Word count: ' + wordCount2 + ' /384';
                });
    
                function countWords(text) {
                    var words = text.trim().split(/\s+/);
                    return words.filter(function(word) {
                        return word.length > 0;
                    }).length;
                }
            });
        </script>
    </div>
    <div style="width:45%;height:700px; display:inline-block;color:black;">
        <textarea id="sentence2" name="sentence2" style="width:100%;height:700px;"></textarea>
        <div id="wordCount2" style="color: white;">Word count: 0</div>
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
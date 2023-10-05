<script lang="ts">
	import { getContext, onMount, tick } from 'svelte';
	import type { Writable } from 'svelte/store';
	import { afterUpdate } from 'svelte';

	import jquery from 'jquery';

	const currentPage = getContext<Writable<string>>('currentPage');
	$currentPage = 'compare';

	//import { json } from 'node:stream/consumers';
	let sentence1 = '';
	let sentence2 = '';
	let sentenceSimilarityResult = '';
	let similarity_score: number = 0;
	var formType = "sentence_similarity";

	let trafficlightVisibile = false;
  
	// Function to check sentence similarity
	async function checkSimilarity() {
		let requestData = {
			form_type: formType,
			sentence1: sentence1,
			sentence2: sentence2
		};
	  try {
		const response = await fetch('http://127.0.0.1:5000/api/sentence-similarity', {	
		method: 'POST',
		headers: {
		  'Content-Type': 'application/json',
		},
		body: JSON.stringify(requestData),
	  });
	  if (response.ok) {
		const data = await response.json();
		sentenceSimilarityResult = data.sentence_similarity_result;
		similarity_score = parseFloat(data.similarity_score);
		similarity_score = similarity_score * 100;

		trafficlightVisibile = true;

		await tick();

		updateTrafficLight(similarity_score);
		updateResponseText(similarity_score);
	  }
	} catch (error) {
		console.error('Error', error);
	}
		}
	function updateTrafficLight(similarity_score: number) {
            var trafficLightDiv = jquery("#traffic_light");



            //trafficLightDiv.removeClass("green yellow red");

			console.log("Current score" + similarity_score);

            if (similarity_score >= 80) {
      			trafficLightDiv.css('background-color', 'green');
    		} else if (similarity_score >= 60) {
      			trafficLightDiv.css('background-color', 'yellow');
			} else {
      			trafficLightDiv.css('background-color', 'red');
    		}
	}
	function updateResponseText(similarity_score: number) {
            var responseText = jquery("#response_text");

            if (similarity_score >= 80) {
                responseText.text("High Similarity: The content is very similar.");
            } else if (similarity_score >= 60) {
                responseText.text("Medium Similarity: There is some similarity in the content.");
            } else {
                responseText.text("Low Similarity: The content is not very similar.");
            }
	}
	onMount(() => {
		});
</script>


  <main>
	<p class="title">Compare Courses (Text Entry)</p>
	<!-- Sentence Textareas -->
	<div class="textarea-container">
		<div class="textarea-group">
			<h1>Federation University Course:</h1>
			<textarea placeholder="Enter Federation University course information here:" style="color: black;" rows="18" cols="80" bind:value={sentence1}></textarea>
		  </div>
		<div class="textarea-group">
			<h1>External University Course:</h1>
			<textarea placeholder="Enter External University course information here:" style="color: black;" rows="18" cols="80" bind:value={sentence2}></textarea>
		</div>
	</div>
  
	<!-- Check Similarity Button -->
	<br>
	<div class="centreelement">
		<button class="comparebutton" id="check_similarity_button" on:click={checkSimilarity}>Check Similarity</button>
	</div>
  
	<!-- Similarity Result Display -->
	{#if sentenceSimilarityResult}
	  <div class="score">{sentenceSimilarityResult}</div>
	  {#if trafficlightVisibile}
		<div class="center-container">
			<div class="response-container">
				<div class="traffic-light" id="traffic_light"></div>
				<div class="response-text-container">
					<p id="response_text"></p>
				</div>
			</div>
		</div>
	  {/if}
	{/if}
	
  </main>

<style>
.title {
	font-size: 40px;
	padding: 30px;
}
.score {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-top: 20px;
  height: 40px;
}
	.textarea-container {
  	display: flex;
  	justify-content: center;
	}
	.textarea-group {
  	display: flex;
  	flex-direction: column;
  	align-items: flex-start;
  	margin-right: 20px; /* Optional: Add some space between text areas */
}
	textarea {
 	width: 100%; /* Adjust the width based on your preference */
  	margin-right: 10px; /* Add some space between text areas */
	}
	.centreelement {
		width: 100%;
		padding: 10px;
	}
	.comparebutton {
		width: 15%;
		display: block;
		height: 50px;
		font-size: 1em;
		font-weight: bold;
		margin: auto;
		border: 1px solid white;
}
	.response-container {
		display: flex;
		align-items: center;
}

	.center-container {
    display: flex;
    justify-content: center;
    align-items: center;
    height: auto;
}

	.response-container {
    display: flex;
    align-items: center;
}

	.traffic-light {
    width: 50px;
    height: 150px;
    border: 2px solid white;
    border-radius: 8px;
    margin-right: 20px;
}
	.response-text-container {
    flex-grow: 1;
}
	.green {
    background-color: green;
}
	.yellow {
    background-color: yellow;
}
	.red {
    background-color: red;
}
</style>

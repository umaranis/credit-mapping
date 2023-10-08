<script lang="ts">
	import { getContext, onMount, tick } from 'svelte';
	import type { Writable } from 'svelte/store';
	import { afterUpdate } from 'svelte';
	import type { PageData } from './$types';

	import jquery from 'jquery';

	const currentPage = getContext<Writable<string>>('currentPage');
	$currentPage = 'compare';

	export let data: PageData;
	let full: string = '';
	if (data && data.courseDesc) {
		for (let i = 0; i < data.courseDesc.length; i++) {
			full += data.courseDesc[i].content + '\n\n';
		}
	}

	let sentence1 = full;
	let sentence2 = '';
	let similarity_score: number = 0;
	var formType = 'sentence_similarity';
	let wordCount1 = 0;
	let wordCount2 = 0;

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
					'Content-Type': 'application/json'
				},
				body: JSON.stringify(requestData)
			});
			if (response.ok) {
				const data = await response.json();
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
		var trafficLightDiv = jquery('#traffic_light');

		//trafficLightDiv.removeClass("green yellow red");

		console.log('Current score' + similarity_score);

		if (similarity_score >= 80) {
			trafficLightDiv.css('background-color', 'green');
		} else if (similarity_score >= 60) {
			trafficLightDiv.css('background-color', 'yellow');
		} else {
			trafficLightDiv.css('background-color', 'red');
		}
	}
	function updateResponseText(similarity_score: number) {
		var responseText = jquery('#response_text');

		if (similarity_score >= 80) {
			responseText.text('High Similarity: The content is very similar.');
		} else if (similarity_score >= 60) {
			responseText.text('Medium Similarity: There is some similarity in the content.');
		} else {
			responseText.text('Low Similarity: The content is not very similar.');
		}
	}
	onMount(() => {
		updateWordCount('sentence1');
		updateWordCount('sentence2');
	});

	//WORD COUNTING
	function updateWordCount(textAreaId) {
		const text = textAreaId === 'sentence1' ? sentence1 : sentence2;
		const words = text.trim().split(/\s+/);
		const count = words.filter((word) => word.length > 0).length;

		if (textAreaId === 'sentence1') {
			wordCount1 = count;
		} else if (textAreaId === 'sentence2') {
			wordCount2 = count;
		}
	}

	//PDF UPLOAD

	let selectedTextarea = 'sentence1';

	async function handleUpload(event) {
		event.preventDefault();

		const formData = new FormData(event.target);

		try {
			const response = await fetch('http://127.0.0.1:5000/api/upload-pdf', {
				method: 'POST',
				body: formData
			});

			if (response.ok) {
				const pdfText = await response.text();
				console.log('PDF Text:', pdfText);

				if (selectedTextarea === 'sentence1') {
					sentence1 = pdfText;
					updateWordCount('sentence1');
				} else if (selectedTextarea === 'sentence2') {
					sentence2 = pdfText;
					updateWordCount('sentence2');
				}

				//if (selectedTextarea)
				//sentence1 = pdfText;
				//updateWordCount('sentence1');
			} else {
				console.error('Error uploading PDF');
			}
		} catch (error) {
			console.error('Error', error);
		}
	}
</script>

<main>
	<p class="title">Compare Courses</p>
	<!-- Sentence Textareas -->
	<div class="textarea-container">
		<div class="textarea-group">
			<h1>Federation University Course: {data.unitid ? data.unitid : ''}</h1>
			<textarea
				id="sentence1"
				placeholder="Enter Federation University course information here:"
				style="color: black;"
				rows="14"
				cols="80"
				bind:value={sentence1}
				on:input={() => updateWordCount('sentence1')}
			/>
			<div id="wordCount1">Word count: {wordCount1} /384</div>
		</div>
		<div class="textarea-group">
			<h1>External University Course:</h1>
			<textarea
				id="sentence2"
				placeholder="Enter External University course information here:"
				style="color: black;"
				rows="14"
				cols="80"
				bind:value={sentence2}
				on:input={() => updateWordCount('sentence2')}
			/>
			<div id="wordCount2">Word count: {wordCount2} /384</div>
		</div>
		<br />
	</div>
	<div class="pdf">
		<form
			class="uploadForm"
			on:submit={handleUpload}
			method="POST"
			enctype="multipart/form-data"
			id="form1"
		>
			<label for="file1">Upload pdf file:</label>
			<input type="file" name="file1" id="file1" accept=".pdf" />
			<br /><br />
			<label for="targetTextarea">Where to upload?:</label>
			<select style="color: black;" bind:value={selectedTextarea} id="targetTextarea">
				<option value="sentence1">Federation University Course</option>
				<option value="sentence2">External University Course</option>
			</select>
			<br /><br />
			<input class="pill" type="submit" value="Upload" />
		</form>
	</div>

	<!-- Check Similarity Button -->
	<br />
	<div class="centreelement">
		<button class="comparebutton" id="check_similarity_button" on:click={checkSimilarity}
			>Check Similarity</button
		>
	</div>

	<!-- Similarity Result Display -->
	{#if similarity_score}
		<div class="score"><b><u>{Math.round(similarity_score)}%</u></b></div>
		{#if trafficlightVisibile}
			<div class="center-container">
				<div class="response-container">
					<div class="traffic-light" id="traffic_light" />
					<div class="response-text-container">
						<p id="response_text" />
					</div>
				</div>
			</div>
		{/if}
	{/if}
</main>

<style>
	.pdf {
		width: 75%;
		border: solid white 1px;
		margin: auto;
		padding-left: 20px;
		padding-right: 20px;
		padding-bottom: 10px;
		margin-top: 20px;
	}
	.pill {
		background-color: #ddd;
		border: none;
		color: black;
		padding: 10px 20px;
		text-align: center;
		text-decoration: none;
		display: inline-block;
		margin: 4px 2px;
		cursor: pointer;
		border-radius: 16px;
		width: 150px;
		margin-left: 20px;
	}
	.uploadForm {
		display: flex;
		align-items: center;
		margin-top: 10px;
	}

	.uploadForm label {
		margin-right: 10px;
	}
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
		width: 200px;
		height: 50px;
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

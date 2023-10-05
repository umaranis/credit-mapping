<script lang="ts">
	import { getContext } from 'svelte';
	import type { Writable } from 'svelte/store';

	const currentPage = getContext<Writable<string>>('currentPage');
	$currentPage = 'compare';

	import { onMount } from 'svelte';
	let sentence1 = '';
	let sentence2 = '';
	let sentenceSimilarityResult = '';
  
	// Function to check sentence similarity
	async function checkSimilarity() {
	  const response = await fetch('/api/sentence-similarity', {	
		method: 'POST',
		headers: {
		  'Content-Type': 'application/json',
		},
		body: new URLSearchParams({
		  sentence1,
		  sentence2,
		}),
	  });
	  const data = await response.json();
	  sentenceSimilarityResult = data.sentence_similarity_result;
	}
</script>

this is compare  
  <main>
	<!-- Sentence Textareas -->
	<textarea style="color: black;" rows="20" cols="50" bind:value={sentence1}></textarea>
	<textarea style="color: black;" rows="20" cols="50" bind:value={sentence2}></textarea>
  
	<!-- Check Similarity Button -->
	<button on:click={checkSimilarity}>Check Similarity</button>
  
	<!-- Similarity Result Display -->
	{#if sentenceSimilarityResult}
	  <div>{sentenceSimilarityResult}</div>
	{/if}
  </main>

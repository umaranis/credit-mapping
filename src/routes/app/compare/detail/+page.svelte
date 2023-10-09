<script lang="ts">
	import type { Writable } from 'svelte/store';
	import { compareResult } from './../store';
	import { getContext } from 'svelte';
	import { getScoreColor } from '$lib/helper';
	import TextContainer from './TextContainer.svelte';

	const currentPage = getContext<Writable<string>>('currentPage');
	$currentPage = 'detail';

	let selectedIndex1: number | null = null;
	let selectedIndex2: number | null = null;

	function handleLineSelection1(e: CustomEvent) {
		if (e.detail.selectedIndex !== null) {
			selectedIndex2 = null;
		}
	}

	function handleLineSelection2(e: CustomEvent) {
		if (e.detail.selectedIndex !== null) {
			selectedIndex1 = null;
		}
	}
</script>

{#if $compareResult}
	<h1 style="text-align: center; font-size: 2em; padding: 1em">
		Similarity Score (Overall): {Math.round($compareResult.final_score)}%
	</h1>
	<main>
		<TextContainer
			heading="Federation University Course:"
			text_lines={$compareResult.text1_lines}
			text_lines_scores={$compareResult.text1_lines_scores}
			bind:selectedIndex={selectedIndex1}
			on:lineSelected={handleLineSelection1}
		/>
		<TextContainer
			heading="Other Institution Course:"
			text_lines={$compareResult.text2_lines}
			text_lines_scores={$compareResult.text2_lines_scores}
			bind:selectedIndex={selectedIndex2}
			on:lineSelected={handleLineSelection2}
		/>
	</main>
{/if}

<style>
	main {
		display: flex;
		padding: 10px;
	}
</style>

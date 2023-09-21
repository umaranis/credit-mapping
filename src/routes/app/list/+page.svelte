<script lang="ts">
	import type { PageData } from './$types';
	import SelectSubdiscipline from './SelectSubdiscipline.svelte';
	import { convertDBtoUIList } from './dataHelper';
	export let data: PageData;

	const subdisciplineList = convertDBtoUIList(data.result);
</script>

<main>
	<h1>List Courses</h1>
	<SelectSubdiscipline flavorOptions={subdisciplineList} />
	{#each data.result as entry}
		<div>
			<div style="text-indent: 10px">
				{JSON.stringify(entry)}
			</div>
		</div>
	{/each}
</main>

<style>
	main {
		padding: 5em;
	}
</style>

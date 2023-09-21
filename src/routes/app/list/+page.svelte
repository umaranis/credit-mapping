<script lang="ts">
	import type { PageData } from './$types';
	import SelectSubdiscipline from './SelectSubdiscipline.svelte';
	export let data: PageData;
</script>

this is list

<div style="width: 400px">
</div>
{#each data.result as entry}
	<div>
		<div style="text-indent: 10px">
			{JSON.stringify(entry)}
		</div>
	</div>
{/each}

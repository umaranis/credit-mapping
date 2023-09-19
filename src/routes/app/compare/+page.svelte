<script lang="ts">
	import { getContext } from 'svelte';
	import type { Writable } from 'svelte/store';

	const currentPage = getContext<Writable<string>>('currentPage');
	$currentPage = 'compare';
</script>

this is compare

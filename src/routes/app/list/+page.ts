import type { PageLoad } from './$types';

export const load = (async () => {
	return {
		post: {
			title: `Title for goes here`,
			content: `Content for goes here`
		}
	};
}) satisfies PageLoad;

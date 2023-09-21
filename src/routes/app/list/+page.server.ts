import { sql } from '$lib/db';
import type { PageServerLoad } from './$types';

export const load = (async () => {
	const users = await sql`
        select
        *
        from creditmap_schema.subdiscipline`;

	return {
		result: users
	};
}) satisfies PageServerLoad;

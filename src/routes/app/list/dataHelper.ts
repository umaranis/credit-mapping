import type postgres from 'postgres';
export function convertDBtoUIList(data: postgres.RowList<postgres.Row[]>) {
	return data.map((row) => {
		return {
			label: row.subdisciplinelongname,
			value: row.subdisciplineid
		};
	});
}

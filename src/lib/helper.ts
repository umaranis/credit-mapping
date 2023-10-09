export function getScoreColor(score: number | null): string | null {
    if (!score) {
		return null;
	} else if (score >= 80) {
		return '#78c47a';
	} else if (score >= 60) {
		return '#f2f291';
	} else {
		return '#eaa4a4';
	}
}



export type CompareResult = {similarity_score: Array<Array<number>>, text1_lines: Array<string>, text2_lines: Array<string>};
export async function checkTextSimilarity(text1: string, text2: string) : Promise<CompareResult | null> {
    try {
        const response = await fetch('http://127.0.0.1:5000/api/text-similarity', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                text1,
                text2
            })
        });
        if (response.ok) {
            return await response.json();            
        } else {
            console.error(response.statusText +  ' - ' + "'text-similarity' api call failed!");
        }
    } catch (error) {
        console.error('Error', error);
    }

    return null;
}


export async function checkSentenceSimilarity(sentence1: string, sentence2: string): Promise<number | null> {
    try {
        const response = await fetch('http://127.0.0.1:5000/api/sentence-similarity', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                sentence1: sentence1,
                sentence2: sentence2
            })
        });
        if (response.ok) {
            const data = await response.json();
            let similarity_score = parseFloat(data.similarity_score);
            similarity_score = similarity_score * 100;
            return similarity_score;
        }
        else {
            console.error(response.statusText +  ' - ' + "'sentence-similarity' api call failed!");
        }

    } catch (error) {
        console.error('Error', error);
    }

    return null;

}
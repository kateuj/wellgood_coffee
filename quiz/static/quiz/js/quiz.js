function showResult() {
    const q1 = document.querySelector('input[name="q1"]:checked');
    const q2 = document.querySelector('input[name="q2"]:checked');
    const q3 = document.querySelector('input[name="q3"]:checked');

    if (!q1 || !q2 || !q3) {
        alert('Please answer all questions.');
        return;
    }

    let recommendation = '';

    if (q1.value === 'espresso' && q2.value === 'caffeinated' && q3.value === 'caramel-chocolate-sweet') {
        recommendation = 'Espresso with steamed milk';
    } else if (q1.value === 'filter' && q2.value === 'decaf' && q3.value === 'floral-rose') {
        recommendation = 'Iced black coffee with almond milk';
    } else if (q1.value === 'whole-bean' && q2.value === 'either' && q3.value === 'fruity-light') {
        recommendation = 'Americano';
    } else if (q1.value === 'cafetiere' && q2.value === 'cold' && q3.value === 'dairy') {
        recommendation = 'Iced caramel latte';
    } else if (q1.value === 'cafetiere' && q2.value === 'cold' && q3.value === 'dairy') {
        recommendation = 'Iced caramel latte';    
    } else {
        recommendation = 'Classic black coffee';
    }

    const resultDiv = document.getElementById('result');
    resultDiv.textContent = 'We recommend: ' + recommendation;
    resultDiv.style.display = 'block';
}
function showResult() {
    const q1 = document.querySelector('input[name="q1"]:checked');
    const q2 = document.querySelector('input[name="q2"]:checked');
    const q3 = document.querySelector('input[name="q3"]:checked');

    if (!q1 || !q2 || !q3) {
        alert('Please answer all questions.');
        return;
    }

    let recommendation = '';

    if (q2.value === 'decaf') {
        recommendation = 'Swiss Water Decaf';
    } else if (q3.value === 'floral-rose') {
        recommendation = 'Sunrise Serenade or Brew-tiful Day';
    } else if (q3.value === 'fruity-light') {
        recommendation = 'Brew-tiful Day or Rocket Fuel';
    } else if (q2.value === 'caffeinated' && q3.value === 'caramel-chocolate-sweet') {
        recommendation = 'Java Joyride, Happy Camper or Perky Panther';
    } else if (q2.value === 'either' && q3.value === 'caramel-chocolate-sweet') {
        recommendation = 'Java Joyride, Happy Camper, Swiss Water Decaf or Perky Panther';
    }

    const resultDiv = document.getElementById('result');
    resultDiv.textContent = 'We recommend: ' + recommendation + ' ' + q1.value;
    resultDiv.style.display = 'block';
}
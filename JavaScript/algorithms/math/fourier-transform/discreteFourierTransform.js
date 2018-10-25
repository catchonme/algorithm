import ComplexNumber from '../complex-number/ComplexNumber';


const CLOSE_TO_ZERO_THRESHOLD = 1e-10;


export default function dft(inputAmplitudes, zeroThreshold = CLOSE_TO_ZERO_THRESHOLD) {
    const N = inputAmplitudes.length;
    const signals = [];

    for (let frequency = 0; frequency < N; frequency += 1) {
        let frequencySingal = new ComplexNumber();

        for (let timer = 0; timer < N; timer += 1) {
            const currentAmplitude = inputAmplitudes[timer];

            const rotationAngle = -1 * (2 * Math.PI) * frequency * (timer / N);

            const dataPointContribution = new ComplexNumber({
                re: Math.cos(rotationAngle),
                im: Math.sin(rotationAngle)
            }).multiply(currentAmplitude);

            frequencySingal = frequencySingal.add(dataPointContribution);
        }

        if (Math.abs(frequencySingal.re) < zeroThreshold) {
            frequencySingal.re = 0;
        }

        if (Math.abs(frequencySingal.im) < zeroThreshold) {
            frequencySingal.im = 0;
        }

        frequencySingal = frequencySingal.divide(N);

        signals[frequency] = frequencySingal;
    }
    
    return signals;
}
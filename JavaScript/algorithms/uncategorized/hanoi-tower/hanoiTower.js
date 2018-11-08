import Stack from '../../../data-structures/stack/Stack';

function hanoiTowerRecursive({
                                 numberOfDiscs,
                                 fromPole,
                                 withPole,
                                 toPole,
                                 moveCallback
                             }) {
    if (numberOfDiscs === 1) {
        moveCallback(fromPole.peek(), fromPole.toArray(), toPole.toArray());
        const disc = fromPole.pop();
        toPole.push(disc);
    } else {
        hanoiTowerRecursive({
            numberOfDiscs: numberOfDiscs - 1,
            fromPole,
            withPole: toPole,
            toPole, withPole,
            moveCallback
        });

        hanoiTowerRecursive({
            numberOfDiscs: 1,
            fromPole,
            withPole,
            toPole,
            moveCallback
        });

        hanoiTowerRecursive({
            numberOfDiscs: numberOfDiscs - 1,
            fromPole: withPole,
            withPole: fromPole,
            toPole,
            moveCallback
        })
    }
}

export default function hanoiTower({
    numberOfDiscs,
    moveCallback,
    fromPole = new Stack(),
    withPole = new Stack(),
    toPole = new Stack()
}) {
    for (let discSize = numberOfDiscs; discSize > 0; discSize -= 1) {
        fromPole.push(discSize);
    }

    hanoiTowerRecursive({
        numberOfDiscs,
        fromPole,
        withPole,
        toPole,
        moveCallback
    })
}
const couleurs = ['CARREAU', 'COEUR', 'TREFLE', 'PIQUE'];
        const noms = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valet', 'Dame', 'Roi', 'As'];
        const valeurs = {
            '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
            'Valet': 11, 'Dame': 12, 'Roi': 13, 'As': 14
        };
    
        let deck = [];
        let joueur1 = [];
        let joueur2 = [];
        let pointsJoueur1 = 0;
        let pointsJoueur2 = 0;
        let partieTerminee = false;
    
        function initializeGame() {
            deck = [];
            for (let couleur of couleurs) {
                for (let nom of noms) {
                    deck.push([nom, couleur]);
                }
            }
            shuffle(deck);
            joueur1 = deck.slice(0, 26);
            joueur2 = deck.slice(26);
            shuffle(joueur1);
            shuffle(joueur2);
            pointsJoueur1 = 0;
            pointsJoueur2 = 0;
            partieTerminee = false;
            document.getElementById('player-score').textContent = pointsJoueur1;
            document.getElementById('pc-score').textContent = pointsJoueur2;
            document.getElementById('player-card').textContent = 'Cliquez pour jouer';
            document.getElementById('pc-card').textContent = 'Carte PC';
        }
    
        function shuffle(array) {
            for (let i = array.length - 1; i > 0; i--) {
                const j = Math.floor(Math.random() * (i + 1));
                [array[i], array[j]] = [array[j], array[i]];
            }
        }
    
        function playRound() {
            if (partieTerminee) return;
            if (joueur1.length === 0 || joueur2.length === 0) {
                terminerPartie();
                return;
            }
    
            const carteJouee1 = joueur1.shift();
            const carteJouee2 = joueur2.shift();
    
            document.getElementById('player-card').textContent = `${carteJouee1[0]}\n${carteJouee1[1]}`;
            document.getElementById('pc-card').textContent = `${carteJouee2[0]}\n${carteJouee2[1]}`;
    
            const valeur1 = valeurs[carteJouee1[0]];
            const valeur2 = valeurs[carteJouee2[0]];
    
            if (valeur1 > valeur2) {
                pointsJoueur1++;
            } else if (valeur2 > valeur1) {
                pointsJoueur2++;
            }
    
            document.getElementById('player-score').textContent = pointsJoueur1;
            document.getElementById('pc-score').textContent = pointsJoueur2;
    
            if (joueur1.length === 0 || joueur2.length === 0) {
                terminerPartie();
            }
        }
    
        function terminerPartie() {
            partieTerminee = true;
            let message = pointsJoueur1 > pointsJoueur2 ? "Joueur 1 gagne la partie !" : pointsJoueur2 > pointsJoueur1 ? "PC gagne la partie !" : "Match nul !";
            alert(message);
        }
    
        document.getElementById('player-card').addEventListener('click', playRound);
        document.getElementById('restart-game').addEventListener('click', initializeGame);
    
        initializeGame();
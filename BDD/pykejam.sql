-- phpMyAdmin SQL Dump
-- version 4.8.3
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1
-- Généré le :  mer. 16 mars 2022 à 10:12
-- Version du serveur :  10.1.36-MariaDB
-- Version de PHP :  7.2.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données :  `pykejam`
--

-- --------------------------------------------------------

--
-- Structure de la table `attaqueautres`
--

CREATE TABLE `attaqueautres` (
  `id` int(11) NOT NULL,
  `attaqueId` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `attaqueautres`
--

INSERT INTO `attaqueautres` (`id`, `attaqueId`) VALUES
(1, 1),
(2, 2),
(3, 8),
(4, 9),
(5, 12),
(6, 15),
(7, 17),
(8, 20),
(9, 21),
(10, 22),
(11, 23),
(12, 24),
(13, 26),
(14, 27),
(15, 31),
(16, 35),
(17, 41),
(18, 43),
(19, 46),
(20, 48),
(21, 50),
(22, 51),
(23, 61),
(24, 67),
(25, 70),
(26, 71),
(27, 75),
(28, 76),
(29, 77),
(30, 78),
(31, 80),
(32, 91),
(33, 93),
(34, 94),
(35, 97),
(36, 98),
(37, 100),
(38, 101),
(39, 103),
(40, 105),
(41, 109),
(42, 113),
(43, 114),
(44, 118),
(45, 119),
(46, 120),
(47, 121),
(48, 127),
(49, 128);

-- --------------------------------------------------------

--
-- Structure de la table `attaquebuff`
--

CREATE TABLE `attaquebuff` (
  `id` int(11) NOT NULL,
  `attaqueId` int(11) DEFAULT NULL,
  `statBuff` varchar(255) DEFAULT NULL,
  `nombreBuff` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `attaquebuff`
--

INSERT INTO `attaquebuff` (`id`, `attaqueId`, `statBuff`, `nombreBuff`) VALUES
(1, 25, 'Def', -1),
(2, 25, 'DefSpe', -1),
(3, 32, 'Att', 1),
(4, 32, 'Speed', 1),
(5, 33, 'Att', 2),
(6, 36, 'AttSpe', -2),
(7, 44, 'Att', 1),
(8, 44, 'Def', 1),
(9, 44, 'accuracy', 1),
(10, 47, 'Att', 2),
(11, 47, 'AttSpe', 2),
(12, 47, 'Speed', 2),
(13, 47, 'Def', -1),
(14, 47, 'DefSpe', -1),
(15, 52, 'Att', 1),
(16, 52, 'Def', 1),
(17, 56, 'Speed', 2),
(18, 66, 'AttSpe', 2),
(19, 73, 'AttSpe', 1),
(20, 73, 'DefSpe', 1),
(21, 73, 'Speed', 1),
(22, 83, 'AttSpe', 1),
(23, 83, 'DefSpe', 1),
(24, 87, 'Speed', 2),
(25, 96, 'Att', 1),
(26, 96, 'AttSpe', 1),
(27, 106, 'AttSpe', -2),
(28, 108, 'Att', -1),
(29, 108, 'Def', -1);

-- --------------------------------------------------------

--
-- Structure de la table `attaqueclimat`
--

CREATE TABLE `attaqueclimat` (
  `id` int(11) NOT NULL,
  `attaqueId` int(11) DEFAULT NULL,
  `climatId` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `attaqueclimat`
--

INSERT INTO `attaqueclimat` (`id`, `attaqueId`, `climatId`) VALUES
(1, 34, 2);

-- --------------------------------------------------------

--
-- Structure de la table `attaqueheal`
--

CREATE TABLE `attaqueheal` (
  `id` int(11) NOT NULL,
  `attaqueId` int(11) DEFAULT NULL,
  `PVHeal` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `attaqueheal`
--

INSERT INTO `attaqueheal` (`id`, `attaqueId`, `PVHeal`) VALUES
(1, 4, 50),
(2, 6, 50),
(3, 39, 50),
(4, 74, 50),
(5, 102, 50);

-- --------------------------------------------------------

--
-- Structure de la table `attaqueoffensive`
--

CREATE TABLE `attaqueoffensive` (
  `id` int(11) NOT NULL,
  `attaqueId` int(11) DEFAULT NULL,
  `puissance` int(11) DEFAULT NULL,
  `physique` tinyint(1) DEFAULT NULL,
  `special` tinyint(1) DEFAULT NULL,
  `priorityLevel` int(11) NOT NULL DEFAULT '0',
  `effect` tinyint(1) DEFAULT '0',
  `probaEffect` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `attaqueoffensive`
--

INSERT INTO `attaqueoffensive` (`id`, `attaqueId`, `puissance`, `physique`, `special`, `priorityLevel`, `effect`, `probaEffect`) VALUES
(1, 3, 85, 1, 0, 0, 1, 20),
(2, 5, 80, 0, 1, 0, 0, NULL),
(3, 7, 60, 1, 0, 0, 0, NULL),
(4, 10, 80, 0, 1, 0, 1, 20),
(5, 11, 80, 1, 0, 0, 0, NULL),
(6, 13, 40, 1, 0, 3, 0, NULL),
(7, 14, 90, 0, 1, 0, 1, 30),
(8, 16, 90, 0, 1, 0, 1, 10),
(9, 18, 95, 0, 1, 0, 1, 10),
(10, 19, 80, 1, 0, 0, 1, 20),
(11, 25, 120, 1, 0, 0, 0, NULL),
(12, 28, 70, 1, 0, 1, 0, NULL),
(13, 29, 80, 0, 1, 0, 1, 30),
(14, 30, 95, 0, 1, 0, 1, 10),
(15, 36, 130, 0, 1, 0, 0, NULL),
(16, 37, 110, 0, 1, 0, 1, 10),
(17, 38, 120, 0, 1, 0, 1, 30),
(18, 40, 80, 0, 1, 0, 1, 30),
(19, 42, 80, 0, 1, 0, 0, NULL),
(20, 45, 120, 1, 0, 0, 1, 10),
(21, 54, 110, 0, 1, 0, 0, NULL),
(22, 55, 90, 1, 0, 0, 0, NULL),
(23, 57, 75, 0, 1, 0, 1, 30),
(24, 58, 100, 1, 0, 0, 1, 100),
(25, 59, 90, 1, 0, 0, 1, 100),
(26, 60, 90, 0, 1, 0, 1, 10),
(27, 62, 90, 0, 1, 0, 1, 10),
(28, 63, 80, 0, 1, 0, 1, 10),
(29, 64, 70, 0, 1, 0, 1, 10),
(30, 65, 40, 1, 0, 1, 0, NULL),
(31, 68, 80, 1, 0, 0, 1, 20),
(32, 69, 120, 1, 0, 0, 0, NULL),
(33, 72, 40, 1, 0, 1, 0, NULL),
(34, 79, 40, 1, 0, 1, 0, NULL),
(35, 81, 80, 1, 0, 0, 0, NULL),
(36, 82, 85, 1, 0, 0, 1, 30),
(37, 84, 75, 1, 0, 0, 1, 10),
(38, 85, 75, 1, 0, 0, 1, 10),
(39, 86, 75, 1, 0, 0, 1, 10),
(40, 89, 80, 1, 0, 0, 0, NULL),
(41, 90, 95, 0, 1, 0, 1, 30),
(42, 92, 90, 0, 1, 0, 1, 10),
(43, 95, 75, 0, 1, 0, 1, 10),
(44, 99, 100, 1, 0, 0, 0, NULL),
(45, 106, 130, 0, 1, 0, 0, NULL),
(46, 107, 90, 0, 1, 0, 0, NULL),
(47, 108, 120, 1, 0, 0, 0, NULL),
(48, 110, 100, 1, 0, 0, 0, NULL),
(49, 111, 90, 0, 1, 0, 1, 10),
(50, 112, 90, 0, 1, 0, 1, 10),
(51, 116, 95, 1, 0, 0, 0, NULL),
(52, 117, 80, 1, 0, 0, 1, 100),
(53, 122, 110, 0, 1, 0, 1, 30),
(54, 123, 60, 0, 1, 0, 1, 20),
(55, 124, 80, 0, 1, 0, 1, 20),
(56, 125, 80, 1, 0, 2, 0, NULL),
(57, 126, 40, 1, 0, 1, 0, NULL);

-- --------------------------------------------------------

--
-- Structure de la table `attaques`
--

CREATE TABLE `attaques` (
  `id` int(11) NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `accuracy` int(11) DEFAULT NULL,
  `typeId` int(11) DEFAULT NULL,
  `description` text,
  `PP` int(11) DEFAULT NULL,
  `offensive` tinyint(1) DEFAULT '0',
  `climat` tinyint(1) DEFAULT '0',
  `heal` tinyint(1) DEFAULT '0',
  `buff` tinyint(1) DEFAULT '0',
  `statut` tinyint(1) DEFAULT '0',
  `autres` tinyint(1) DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `attaques`
--

INSERT INTO `attaques` (`id`, `name`, `accuracy`, `typeId`, `description`, `PP`, `offensive`, `climat`, `heal`, `buff`, `statut`, `autres`) VALUES
(1, 'Abri', 70, 1, 'Abri protège de tout effet, direct ou indirect, qu\'une capacité adverse pourrait causer. Ceci n\'inclut pas les dégâts causés par un éventuel changement de climat ou de statut. Elle n\'empêche pas non plus la pose des pièges d\'entrée. Si le Pokémon qui utilise Abri attaque en dernier, la capacité échoue nécessairement.', 10, 0, 0, 0, 0, 0, 1),
(2, 'Anti-Brume', NULL, 10, 'Cette attaque enlève le climat actuel', 15, 0, 0, 0, 0, 0, 1),
(3, 'Aqua-Brèche', 100, 3, 'Aqua-Brèche inflige des dégâts et a 20% de chance de baisser la défense de la cible.', 10, 1, 0, 0, 0, 0, 0),
(4, 'Atterrissage', NULL, 10, 'Atterrissage restaure jusqu\'à la moitié des PV maximum du lanceur.', 10, 0, 0, 1, 0, 0, 0),
(5, 'Aurasphère', NULL, 7, 'Aurasphère inflige des dégâts avec une précision inaltérable. Elle n\'échoue que si la cible se protège avec une capacité comme Abri ', 20, 1, 0, 0, 0, 0, 0),
(6, 'Aurore', NULL, 1, 'Aurore restaure la moitié des PV max du lanceur.', 5, 0, 0, 1, 0, 0, 0),
(7, 'Aéropique', NULL, 10, 'Aéropique inflige des dégâts sans prendre en compte d\'éventuelles modifications de la précision ou de l\'esquive de la cible ou du lanceur, étant une capacité qui n\'échoue jamais.', 20, 1, 0, 0, 0, 0, 0),
(8, 'Balance', NULL, 1, 'Balance additionne le nombre de PV de l\'utilisateur à celui de l\'adversaire et divise cette somme par deux, le résultat devient le nombre de PV de chacun des deux Pokémon. Si cette valeur est supérieure aux PV de l\'un des Pokémon, celui-ci aura sa jauge de PV remplie.\r\n\r\nCette capacité ne prend pas en compte les changements de précision/esquive.', 20, 0, 0, 0, 0, 0, 1),
(9, 'Ball\'Meteo', 100, 1, 'Si aucune modification du climat n\'est en cours, Ball\'Météo possède une puissance de 50 et inflige des dégâts de type Normal.\r\n\r\nSi une modification de climat est en cours, Ball\'Météo voit sa puissance doublée pour monter à 100 et son type modifié en fonction du climat rencontré :\r\n\r\nEn cas d\'ensoleillement (exemple : utilisation de Zénith), Ball\'Météo fait des dégâts de type Feu ;\r\nEn cas de pluie (exemple : utilisation de Danse Pluie), Ball\'Météo fait des dégâts de type Eau ;\r\nEn cas de grêle, Ball\'Météo fait des dégâts de type Glace ;\r\nEn cas de tempête de sable, Ball\'Météo fait des dégâts de type Roche ;\r\nEn cas de brouillard, Ball\'Météo reste de type Normal (tout en ayant une puissance double).', 10, 0, 0, 0, 0, 0, 1),
(10, 'Ball\'Ombre', 100, 14, 'Ball\'Ombre inflige des dégâts et a 20 % de chances de baisser d\'un niveau la Défense Spéciale de la cible.', 15, 1, 0, 0, 0, 0, 0),
(11, 'Bec Vrille', 100, 10, 'Bec Vrille inflige des dégâts, sans effets secondaires.', 20, 1, 0, 0, 0, 0, 0),
(12, 'Blabla Dodo', NULL, 1, 'Blabla Dodo permet au lanceur d\'utiliser une capacité au hasard parmi son panel de capacités lorsqu\'il est endormi. La capacité ne fonctionne donc uniquement que lorsque le lanceur est endormi.', 10, 0, 0, 0, 0, 0, 1),
(13, 'Bluff', 100, 1, 'Bluff frappe en premier, inflige des dommages au Pokémon adverse et l\'apeure. Cependant, cette capacité ne peut être utilisée qu\'au tour d\'arrivée du lanceur.', 10, 1, 0, 0, 0, 0, 0),
(14, 'Bomb Beurk', 100, 8, 'Bombe Beurk inflige des dégâts et a 30% de chances d\'empoisonner la cible.', 10, 1, 0, 0, 0, 0, 0),
(15, 'Boule Roc', 90, 13, 'Boule Roc inflige des dommages de deux à cinq fois. Il y a 37,5% de chances que la capacité fasse 2 coups, 37,5% de chances qu\'elle fasse 3 coups, 12,5% de chances qu\'elle fasse 4 coups et 12,5% de chances qu\'elle fasse 5 coups. Tous les coups de Boule Roc peuvent potentiellement faire un coup critique. Boule Roc peut continuer même après avoir brisé un clone. Riposte et Patience prennent en considération le dernier coup porté uniquement.\r\n\r\nSi la Ceinture Force, le Bandeau ou la capacité spéciale Fermeté s\'active avant que le dernier coup de Boule Roc soit asséné, la cible est K.O.', 10, 0, 0, 0, 0, 0, 1),
(16, 'Bourdon', 100, 12, 'Bourdon inflige des dommages et possède 10 % de chances de diminuer d\'un niveau la Défense Spéciale de la cible.', 10, 1, 0, 0, 0, 0, 0),
(17, 'Boutefeu', 100, 2, 'Boutefeu dégèle le lanceur et inflige des dégâts à l\'adversaire. Le lanceur reçoit un contrecoup égal à 1/3 des dégâts infligés par la capacité. Cette capacité a 10% de chances de brûler l\'adversaire.', 15, 0, 0, 0, 0, 0, 1),
(18, 'Canicule', 90, 2, 'Canicule a 10% de chances de brûler la cible (si elle n\'est pas déjà atteinte par un changement de statut).', 10, 1, 0, 0, 0, 0, 0),
(19, 'Cascade', 100, 3, 'Cascade inflige des dégâts et a 20 % de chances d\'apeurer la cible.', 15, 1, 0, 0, 0, 0, 0),
(20, 'Casse-Brique', 100, 7, 'Casse-Brique inflige des dégâts et annule les effets de Mur Lumière et/ou de Protection même si Casse-Brique échoue. Cependant, Casse-Brique n\'annule pas les effets de Mur Lumière et/ou de Protection si la cible est de type Spectre.', 15, 0, 0, 0, 0, 0, 1),
(21, 'Change Éclair', 100, 5, 'L\'utilisateur de Change Éclair attaque, puis se retire immédiatement. Il ne se retire pas s\'il est le seul de l\'équipe encore debout ou si le fait d\'avoir utilisé Demi-Tour a mis fin au combat.', 20, 0, 0, 0, 0, 0, 1),
(22, 'Choc Psy', 100, 11, 'Cette capacité utilise l\'Attaque Spéciale du lanceur et la défense de la cible pour frapper ; elle inflige donc des dégâts physiques.', 10, 0, 0, 0, 0, 0, 1),
(23, 'Clairvoyance', NULL, 1, 'Clairvoyance annule les immunités du type Spectre de la cible et permet donc de frapper des Pokémon Spectre avec des capacités de type Normal ou Combat, tout en ramenant l\'esquive de la cible à 0. L\'effet de Clairvoyance est annulé si la cible touchée est changée ou retirée du combat, mais l\'effet perdure si le lanceur de la capacité change ou est retiré.', 40, 0, 0, 0, 0, 0, 1),
(24, 'Clonage', NULL, 1, 'En sacrifiant 25% de ses PV maximum, le lanceur crée un clone, copie conforme du point de vue du type et des statistiques. Les PV du clone sont ceux perdus par le lanceur pour l\'utiliser. Par exemple, si un Pokémon perd 56 PV pour la création du clone, le clone a 56 PV.\r\n\r\nUne fois le clone créé, celui-ci prendra les dégâts causés par l\'adversaire à la place du lanceur, jusqu\'à sa destruction. Le clone prend aussi les capacités de statut (telles que Cage-Éclair et Onde Folie) et de diminution de statistiques (telles que Jet de Sable) lancées après son apparition, ce qui en immunise son lanceur tant que le clone est présent.\r\n\r\nSi le clone est détruit par une capacité drainant des PV, les PV sont drainés du clone.\r\n\r\nClonage ne protège pas des effets de Requiem, Provoc, Entrave, Encore, Tourmente, Dépit, Buée Noire, Boost, Saisie, Échange, Imitation, Cyclone et Hurlement, ni des capacités sonores, mais bloque Regard Noir, Tourmagik (et leurs équivalents), Anti-Soin, Embargo, Échange Psy ou encore Balance. Le clone bloque la réduction de statistiques d\'Anti-Brume, mais n\'empêche pas les autres effets de cette capacité.\r\n\r\nSi les PV du lanceur sont inférieurs ou égaux à 25% de ses PV maximum, Clonage échoue. De fait, Munja ne peut utiliser Clonage, puisqu\'il n\'a qu\'un PV, bien qu\'il puisse l\'apprendre.\r\n\r\nLe clone peut être transmis par Relais, mais il conserve les PV qu\'ils lui restent.\r\n\r\nLes capacités comme Toxik ou Onde Folie n\'affectent pas le clone, mais le statut du Pokémon qui a lancé Clonage est affecté par Synchro.', 10, 0, 0, 0, 0, 0, 1),
(25, 'Close Combat', 100, 7, 'Close Combat a pour effet de faire baisser les statistiques de Défense et de Défense Spéciale du lanceur d\'un niveau.', 5, 1, 0, 0, 1, 0, 0),
(26, 'Colère', 100, 15, 'Colère dure deux à trois tours, empêchant toute autre action (y compris le changement de Pokémon et l\'usage d\'objet) tant qu\'elle n\'a pas cessé, et cible un Pokémon adverse au hasard à chaque tour.\r\n\r\nLorsque Colère s\'achève, le Pokémon lanceur devient confus.\r\n\r\nIl est à noter qu\'un seul PP est utilisé par lancement (pour tous les tours).\r\n\r\nSi le dernier tour de Colère est interrompu par un échec, la capacité s\'arrête et le Pokémon lanceur de Colère ne devient pas confus. Cependant, si la capacité est interrompue par Détection ou Abri, le lanceur devient confus comme s\'il avait achevé sa capacité.', 10, 0, 0, 0, 0, 0, 1),
(27, 'Conversion', NULL, 1, 'Le type de l\'utilisateur de cette capacité devient celui de la première capacité dans le moveset du Pokémon.', 30, 0, 0, 0, 0, 0, 1),
(28, 'Coup Bas', 100, 16, 'Inflige des dégâts et attaque toujours en premier, sauf si la cible utilise aussi une capacité de priorité ; dans ce cas, le premier à attaquer est déterminé normalement.\r\n\r\nSi l\'adversaire utilise une capacité non-offensive ou parvient à attaquer avant l\'utilisateur, Coup Bas échoue.', 5, 1, 0, 0, 0, 0, 0),
(29, 'Coup d\'Jus', 100, 5, 'Coup d\'Jus inflige des dégâts et a 30% de chances de paralyser la cible.', 15, 1, 0, 0, 0, 0, 0),
(30, 'Cradovague', 100, 8, 'Cradovague inflige des dégâts avec une puissance de base de 95. Cette capacité a, de plus, 10% de chances d\'empoisonner les cibles.', 10, 1, 0, 0, 0, 0, 0),
(31, 'Damoclès', 100, 1, 'Le lanceur subit 1/3 des dégâts infligés au Pokémon défenseur en tant que contrecoup.', 15, 0, 0, 0, 0, 0, 1),
(32, 'Danse Draco', NULL, 15, 'Danse Draco augmente l\'attaque et la vitesse du lanceur d\'un niveau.', 20, 0, 0, 0, 1, 0, 0),
(33, 'Danse Lames', NULL, 1, 'Danse Lames augmente l\'Attaque de l\'utilisateur de deux niveaux.', 20, 0, 0, 0, 1, 0, 0),
(34, 'Danse Pluie', NULL, 3, 'Lorsque cette capacité est utilisée, une pluie torrentielle s\'enclenche sur le terrain durant 5 tours. Cette pluie provoque plusieurs effets :\r\n\r\nLa puissance des capacités de type Eau est augmentée de 50% et celle des capacités de type Feu diminuée de 50%.\r\nLa puissance de Lance-Soleil est diminuée de 50%.\r\nLa précision de Fatal-Foudre et de Vent Violent passe à 100%.\r\nAurore, Synthèse et Rayon Lune ne restaurent plus qu\'un quart des PV maximum du Pokémon.\r\nUn Pokémon possédant la Capacité Spéciale Cuvette récupère 1/16ème de ses Points de Vie maximum à la fin de chaque tour.\r\nUn Pokémon possédant la capacité spéciale Glissade verra sa Vitesse doublée.\r\nLa capacité Ball\'Météo sera de type Eau et doublera de puissance, tandis que Morphéo gagnera le type Eau lui aussi.\r\nLes Pokémon possédant la Capacité Spéciale Peau Sèche récupèrent 1/8ème de leurs PV maximum à la fin de chaque tour.\r\nL\'objet Roche Humide permet de faire passer la durée de la capacité de 5 à 8 tours.', 5, 0, 1, 0, 0, 0, 0),
(35, 'Demi-Tour', 100, 12, 'L\'utilisateur de Demi-Tour attaque, puis se retire immédiatement. Il ne se retire pas s\'il est le seul de l\'équipe encore debout ou si le fait d\'avoir utilisé Demi-Tour a mis fin au combat.', 20, 0, 0, 0, 0, 0, 1),
(36, 'Draco-Météore', 90, 15, 'Draco-Météore inflige des dommages et réduit ensuite l\'Attaque Spéciale du lanceur de deux niveaux.', 5, 1, 0, 0, 1, 0, 0),
(37, 'Déflagration', 85, 2, 'Déflagration inflige des dégâts et a 10% de chances de brûler la cible.', 5, 1, 0, 0, 0, 0, 0),
(38, 'Détricanon', 80, 8, 'Détricanon inflige des dégâts et a 30% de chances d\'empoisonner la cible.', 5, 1, 0, 0, 0, 0, 0),
(39, 'E-Coque', 100, 1, 'E-Coque restaure jusqu\'à 50% des PV maximum du lanceur, la capacité échoue si les PV du lanceur sont déjà au maximum.', 10, 0, 0, 1, 0, 0, 0),
(40, 'Ébullition', 100, 3, 'Ébullition inflige des dégâts, et possède 30% de chances de brûler la cible.', 15, 1, 0, 0, 0, 0, 0),
(41, 'Éclair Fou', 100, 5, 'Éclair Fou est une capacité qui rejoint la lignée de Bélier ou de Sacrifice : d\'une puissance de 90, elle inflige le quart des dégâts provoqués par la capacité au lanceur.', 15, 0, 0, 0, 0, 0, 1),
(42, 'Éclat Magique', 100, 18, 'Éclat Magique inflige des dégâts, sans effets secondaires.', 10, 1, 0, 0, 0, 0, 0),
(43, 'Effort', 100, 1, 'Effort permet de retirer des PV de la cible pour qu\'ils soient égaux à ceux de l\'utilisateur. Effort échouera si les PV restants de l\'utilisateur sont supérieurs à ceux de la cible.', 5, 0, 0, 0, 0, 0, 1),
(44, 'Enroulement', NULL, 8, 'Enroulement augmente l\'Attaque, la Défense et la Précision du lanceur d\'un niveau.', 20, 0, 0, 0, 1, 0, 0),
(45, 'Exploforce', 70, 7, 'Exploforce possède 10% de chances de baisser la Défense Spéciale adverse et inflige de gros dégâts.', 5, 1, 0, 0, 0, 0, 0),
(46, 'Explosion', 100, 1, 'Explosion inflige des dégâts et provoque le K.O. de l\'utilisateur, que le coup ait porté ou non.', 5, 0, 0, 0, 0, 0, 1),
(47, 'Exuviation', NULL, 1, 'Exuviation est une capacité qui fait gagner deux niveaux d\'Attaque, Attaque Spéciale et Vitesse à son lanceur. En contrepartie, ce dernier perd un niveau de Défense et de Défense Spéciale.', 15, 0, 0, 0, 1, 0, 0),
(48, 'Façade', 100, 1, 'Façade inflige des dommages. Sa puissance de base devient 140 si l\'utilisateur est empoisonné, paralysé ou brûlé. La baisse de l\'attaque due à la brûlure est ignorée.', 20, 0, 0, 0, 0, 0, 1),
(49, 'Feu Follet', 85, 2, 'Feu Follet brûle la cible. La capacité est sans effet sur les types Feu ;', 15, 0, 0, 0, 0, 1, 0),
(50, 'Frappe Atlas', 100, 7, 'Frappe Atlas inflige 100 de dégâts à la cible.', 20, 0, 0, 0, 0, 0, 1),
(51, 'Glas de Soin', NULL, 1, 'Tous les Pokémon présents dans l\'équipe de l\'utilisateur de Glas de Soin seront soignés de la brûlure, du gel, de la paralysie, du poison et du sommeil.', 5, 0, 0, 0, 0, 0, 1),
(52, 'Gonflette', NULL, 7, 'Gonflette monte l\'Attaque et la Défense d\'un niveau.', 20, 0, 0, 0, 1, 0, 0),
(53, 'Grobisou', 75, 1, 'Grobisou endort la cible.', 10, 0, 0, 0, 0, 1, 0),
(54, 'Hydrocanon', 80, 3, 'Hydrocanon inflige des dégâts, sans effet secondaire.', 5, 1, 0, 0, 0, 0, 0),
(55, 'Hydroqueue', 90, 3, 'Hydro-Queue inflige des dégâts, sans effets secondaires.', 5, 1, 0, 0, 0, 0, 0),
(56, 'Hâte', NULL, 11, 'Hâte augmente de deux niveaux la Vitesse du Pokémon lanceur.', 30, 0, 0, 0, 1, 0, 0),
(57, 'Lame d\'Air', 95, 10, 'Lame d\'Air inflige des dommages et possède 30% de chances d\'apeurer la cible.', 15, 1, 0, 0, 0, 0, 0),
(58, 'Lame de Roc', 80, 13, 'Lame de Roc inflige des dégâts et possède un taux de coup critique élevé.', 5, 1, 0, 0, 0, 0, 0),
(59, 'Lame Feuille', 100, 4, 'Lame Feuille tranche l\'ennemi avec une feuille. La capacité dispose d\'un taux de Coup critique élevé.', 15, 1, 0, 0, 0, 0, 0),
(60, 'Lance-Flammes', 100, 2, 'Lance-Flamme possède une puissance de 90. Elle possède 10% de chances de brûler l\'adversaire.', 15, 1, 0, 0, 0, 0, 0),
(61, 'Lance-Soleil', 100, 4, 'Lance-Soleil se déroule normalement en deux tours : le Pokémon absorbe de l\'énergie solaire au premier tour, puis la relâche en un puissant faisceau au second.\r\n\r\nLance-Soleil ne prend cependant qu\'un seul tour d\'utilisation si la capacité Zénith a été lancée auparavant, tandis que l\'utilisation préalable de Danse Pluie, Grêle ou de Tempête de Sable réduit les dégâts de moitié.', 10, 0, 0, 0, 0, 0, 1),
(62, 'Laser Glace', 100, 6, 'Laser Glace possède une puissance de 90. Elle possède aussi 10 % de chances de geler l\'ennemi.', 10, 1, 0, 0, 0, 0, 0),
(63, 'Luminocanon', 100, 17, 'Luminocanon inflige des dégâts et possède 10% de chances de réduire d\'un niveau la Défense Spéciale de la cible.', 10, 1, 0, 0, 0, 0, 0),
(64, 'Lyophilisation', 100, 17, 'Lyophilisation est une capacité ayant 10% de chances de geler la cible.', 20, 1, 0, 0, 0, 0, 0),
(65, 'Mach Punch', 100, 7, 'Si la cible n\'utilise pas de capacité prioritaire durant le tour où la capacité est utilisée, le lanceur frappe en premier, indépendamment de la vitesse du lanceur ou de celle de la cible. Si la cible utilise également une capacité prioritaire durant le tour où Mach Punch est lancé, l\'ordre des capacités est déterminé normalement, selon la vitesse de chacun.', 30, 1, 0, 0, 0, 0, 0),
(66, 'Machination', 100, 16, 'Machination augmente l\'Attaque Spéciale du lanceur de deux niveaux.', 20, 0, 0, 0, 1, 0, 0),
(67, 'Malédiction', NULL, 14, 'Si le lanceur est de type Spectre\r\nLe lanceur perd la moitié de ses PV maximaux et maudit la cible.\r\nLorsqu\'un Pokémon est maudit, il perd un quart de sa vie à chaque tour. Cet effet disparaît avec le switch. Malédiction, en tant que capacité de type Spectre, ne tient pas compte des variations de statistiques du lanceur et de la cible, notamment l\'Esquive et la Précision. Elle passe les clones, ignore les effets de la capacité Abri, et est transmise par la capacité Relais. Les Pokémon possédant le talent Garde Magik peuvent être maudits : ils ne subissent pas les dégâts de la malédiction, mais peuvent par la suite la transmettre via Relais.\r\n\r\nSi le lanceur n\'est pas de type Spectre\r\nAugmente d\'un niveau l\'Attaque et la Défense, mais baisse d\'un niveau la vitesse du lanceur.\r\nUn Pokémon qui utilise cette forme de malédiction est un Curser.', 10, 0, 0, 0, 0, 0, 1),
(68, 'Mâchouille', 100, 14, 'Mâchouille inflige des dégâts et a 20% de chances de baisser la défense de la cible d\'un niveau. Comme Mâchouille est une capacité physique, les dégâts occasionnés peuvent ainsi augmenter d\'un coup sur l\'autre.', 15, 1, 0, 0, 0, 0, 0),
(69, 'Mégacorne', 85, 12, 'Mégacorne inflige des dégâts, sans effets secondaires. C\'est la capacité la plus puissante de type Insecte.', 10, 1, 0, 0, 0, 0, 0),
(70, 'Mégaphone', 100, 1, 'Mégaphone inflige des dégâts, sans effets secondaires. Les dégâts de cette capacité contournent le Clonage.', 10, 0, 0, 0, 0, 0, 1),
(71, 'Noeud Herbe', 100, 4, 'Nœud Herbe fait pousser de l\'herbe sous l\'ennemi pour le faire trébucher. Plus le Pokémon adverse est lourd, plus cette capacité est puissante.', 20, 0, 0, 0, 0, 0, 1),
(72, 'Ombre Portée', 100, 14, 'Ombre Portée est une capacité à priorité accrue : face à une capacité standard, Ombre Portée frappe toujours en premier. Si l\'adversaire utilise également une capacité à priorité accrue, comme Vive-Attaque, l\'ordre dans lequel se déroule les capacités est déterminé par la Vitesse respective des deux adversaires, comme pour deux capacités classiques.', 30, 1, 0, 0, 0, 0, 0),
(73, 'Papillodanse', NULL, 12, 'Papillodanse permet de gagner un niveau d\'Attaque Spéciale, Défense Spéciale et Vitesse.', 20, 0, 0, 0, 1, 0, 0),
(74, 'Paresse', NULL, 1, 'L\'utilisateur de Paresse récupère jusqu\'à la moitié de ses PV totaux.', 10, 0, 0, 1, 0, 0, 0),
(75, 'Picots', NULL, 9, 'Picots inflige des dégâts à tout Pokémon de l\'équipe adverse entrant sur le terrain. Lancer Picots une fois enlève 12,5% des PV max, lancer Picots deux fois enlève 16,66% des PV max et lancer Picots trois fois enlève 25% des PV max à un adversaire entrant sur le terrain. Lancer Picots plus de trois fois échoue.', 20, 0, 0, 0, 0, 0, 1),
(76, 'Pics Toxik', NULL, 8, 'Pics Toxik répand des pics empoisonnés autour de la cible. Si Pics Toxik a été lancé une fois, la cible arrivant sur le terrain est empoisonnée. Si Pics Toxik a été lancé deux fois, la cible arrivant sur le terrain est gravement empoisonnée.\r\n\r\nLes Pokémon de type Vol, Acier ou Poison ne sont pas affectés par cette capacité. De même, les talents Lévitation, Vaccin ou Garde Magik y sont immunisés, tout comme les porteurs des Grosses Bottes.', 20, 0, 0, 0, 0, 0, 1),
(77, 'Pied Sauté', 95, 7, 'Pied Sauté inflige des dégâts. Si la capacité échoue, le lanceur prend des dégâts (la moitié de ses PV maximum). Si elle est lancée contre un Pokémon de type Spectre, la capacité échoue et donc le lanceur prend également des dégâts.', 10, 0, 0, 0, 0, 0, 1),
(78, 'Pied Voltige', 90, 7, 'Pied Voltige inflige des dégâts. Si la capacité échoue, les dégâts causés au lanceur sont égaux à la moitié de ses PV maximum.\r\nLa capacité échoue toujours si lancée contre un Pokémon de type Spectre et donc le lanceur prend les dommages correspondants.', 10, 0, 0, 0, 0, 0, 1),
(79, 'Pisto-Poing', 100, 17, 'Pisto-Poing est une capacité à priorité de niveau 1. Si l\'adversaire attaque aussi avec une capacité de ce niveau de priorité, la vitesse des deux détermine le premier attaquant.', 30, 1, 0, 0, 0, 0, 0),
(80, 'Piège de Roc', NULL, 13, 'Piège de Roc fonctionne sur le même principe que Picots : à chaque changement de Pokémon adverse, le Pokémon apparu perd des PV. Cependant, contrairement à cette dernière, elle affecte tous les Pokémon, y compris ceux de type Vol ou dotés du talent Lévitation, leur infligeant des dégâts en fonction de leur sensibilité au type Roche.', 20, 0, 0, 0, 0, 0, 1),
(81, 'Plaie-Croix', 100, 12, 'Plaie Croix inflige des dommages. Cette capacité n\'a pas d\'effet secondaire.', 15, 1, 0, 0, 0, 0, 0),
(82, 'Plaquage', 100, 1, 'Plaquage inflige des dégâts et a 30% de chances de paralyser le Pokémon adverse, à moins qu\'il ne s\'agisse d\'un Pokémon de type Électrik.', 15, 1, 0, 0, 0, 0, 0),
(83, 'Plénitude', NULL, 11, 'Plénitude augmente à la fois l\'Attaque Spéciale et la Défense Spéciale de l\'utilisateur d\'un cran.', 20, 0, 0, 0, 1, 0, 0),
(84, 'Poing Glace', 100, 6, 'Poing Glace inflige des dégâts et possède 10% de chances de geler la cible sauf si celle-ci est déjà victime d\'un problème de statut majeur comme la paralysie ou derrière un clone.', 15, 1, 0, 0, 0, 0, 0),
(85, 'Poing Feu', 100, 2, 'Poing Feu inflige des dégâts et possède 10% de chances de brûler la cible.', 15, 1, 0, 0, 0, 0, 0),
(86, 'Poing Éclair', 100, 5, 'Poing Éclair inflige des dégâts et possède 10% de chances de paralyser la cible sauf si celle-ci est déjà victime d\'un problème de statut majeur ou derrière un clone.', 15, 1, 0, 0, 0, 0, 0),
(87, 'Poliroche', 100, 13, 'Poliroche augmente la vitesse du lanceur de deux niveaux.', 20, 0, 0, 0, 1, 0, 0),
(88, 'Poudre Dodo', 75, 4, 'Poudre Dodo endort la cible, sauf si celle-ci est déjà victime d\'un problème de statut majeur ou derrière un clone.\r\nLes effets de Poudre Dodo sont inefficaces sur un Pokémon de type Plante.', 15, 0, 0, 0, 0, 1, 0),
(89, 'Poursuite', 100, 16, 'Cette attaque a une puissance de 80 sans restriction.', 20, 1, 0, 0, 0, 0, 0),
(90, 'Pouvoir Lunaire', 100, 18, 'Pouvoir Lunaire inflige des dégâts, et a 30% de chances de baisser l\'Attaque Spéciale de la cible.', 15, 1, 0, 0, 0, 0, 0),
(91, 'Projection', 90, 7, 'À la façon de Draco-Queue, Projection permet de repousser un Pokémon ennemi.  Contre un Dresseur, elle remplace simplement le Pokémon par un autre.\r\n\r\nSi le Pokémon adverse a Ventouse, a lancé Racines ou Clonage, si le Dresseur adverse n\'a qu\'un Pokémon, Projection échoue.\r\n\r\nProjection a une priorité minimale, de l\'ordre de -6. Son lanceur frappe donc toujours en dernier.', 10, 0, 0, 0, 0, 0, 1),
(92, 'Psyko', 100, 11, 'Psyko inflige des dégâts et possède 10% de chances de baisser d\'un niveau la Défense Spéciale de la cible.', 10, 1, 0, 0, 0, 0, 0),
(93, 'Puissance Cachée', 100, NULL, 'Le type de cette capacité est variable selon le pokemon.', 15, 0, 0, 0, 0, 0, 1),
(94, 'Rapace', 100, 11, 'Rapace inflige des dégâts et fait subir au lanceur le tiers des dégâts infligés à la cible.', 15, 0, 0, 0, 0, 0, 1),
(95, 'Rayon Signal', 100, 12, 'Rayon Signal inflige des dégâts et a 10% de chances de rendre la cible confuse.', 15, 1, 0, 0, 0, 0, 0),
(96, 'Rengorgement', NULL, 1, 'Rengorgement est une capacité de boost. Plus précisément, elle augmente d\'un niveau l\'Attaque et l\'Attaque Spéciale du lanceur.', 30, 0, 0, 0, 1, 0, 0),
(97, 'Repos', NULL, 11, 'Le lanceur de Repos s\'endort pendant deux tours, restaure tous ses PV et ses problèmes de statut sont remplacés par le Sommeil.', 10, 0, 0, 0, 0, 0, 1),
(98, 'Requiem', NULL, 1, 'Lorsque Requiem est lancé, tous les Pokémon présents à ce moment sur le terrain sont affectés. Tous les Pokémon affectés sont K.O. 3 tours plus tard (un compte à rebours apparaît à la fin de chaque tour). Si un ou plusieurs Pokémon est retiré entre temps, ce ou ces Pokémon n\'est plus affecté.', 5, 0, 0, 0, 0, 0, 1),
(99, 'Retour', 100, 1, 'Retour a une puissance de 100.', 20, 1, 0, 0, 0, 0, 0),
(100, 'Sabotage', 100, 16, 'Sabotage inflige des dégâts et retire du combat l\'objet tenu par la cible.', 20, 0, 0, 0, 0, 0, 1),
(101, 'Siphon', 85, 3, 'En combat, Siphon enlève 1/8 des PV maximum chez la cible, de quatre à cinq tours, en plus des dégâts occasionnés quand la capacité est utilisée.', 15, 0, 0, 0, 0, 0, 1),
(102, 'Soin', 100, 1, 'Soin permet au lanceur de récupérer jusqu\'à la moitié de ses PV totaux.', 10, 0, 0, 1, 0, 0, 0),
(103, 'Souvenir', 100, 16, 'Souvenir met le lanceur K.O. et fait baisser de deux niveaux l\'Attaque et l\'Attaque Spéciale de la cible.', 10, 0, 0, 0, 0, 0, 1),
(104, 'Spore', 100, 4, 'Spore endort la cible. Spore ne pourra pas fonctionner si la cible a déjà un problème de statut majeur comme la paralysie, le gel, l\'empoisonnement ou la brûlure.', 15, 0, 0, 0, 0, 1, 0),
(105, 'Stalagtite', 100, 6, 'Stalactite attaque de deux à cinq fois par tour (3/8èmes de chances pour frapper 2 fois, 3/8èmes de chances pour frapper 3 fois, 1/8ème de chance pour frapper 4 fois et 1/8ème de chance pour frapper 5 fois).', 30, 0, 0, 0, 0, 0, 1),
(106, 'Surchauffe', 90, 2, 'Surchauffe a été le précurseur de nombreuses capacités telles que Tempête Verte : d\'une puissance de 130 et d\'une précision de 90%, elle baisse de deux niveaux l\'Attaque Spéciale du lanceur.', 5, 1, 0, 0, 1, 0, 0),
(107, 'Surf', 100, 3, 'Surf a une puissance de 90.', 15, 1, 0, 0, 0, 0, 0),
(108, 'Surpuissance', 100, 7, 'Surpuissance inflige des dégâts et réduit l\'Attaque et la Défense du lanceur d\'un niveau.', 5, 1, 0, 0, 1, 0, 0),
(109, 'Synthèse', NULL, 4, 'Synthèse restaure les PV en fonction du climat et de l\'heure de la journée. En temps normal (en pleine journée, sans conditions météo particulières) Synthèse restaure la moitié des PV de l\'utilisateur. Si le soleil brille, Synthèse restaure 2/3 des PV max. Sous les autres conditions météo, Synthèse ne restaure qu\'1/4 des PV max de l\'utilisateur.', 5, 0, 0, 0, 0, 0, 1),
(110, 'Séisme', 100, 9, 'Séisme inflige de lourds dégâts.', 10, 1, 0, 0, 0, 0, 0),
(111, 'Telluriforce', 100, 9, 'Telluriforce inflige des dégâts et possède 10% de chances de baisser la Défense Spéciale de la cible d\'un niveau.', 10, 1, 0, 0, 0, 0, 0),
(112, 'Tonnerre', 100, 5, 'Tonnerre a 10 % de chances de paralyser l\'adversaire, sauf s\'il est cloné ou déjà affecté par une modification de statut.', 15, 1, 0, 0, 0, 0, 0),
(113, 'Tour de Magie', 100, 11, 'Le lanceur échange son objet avec celui de la cible. La capacité échoue si la cible ne tient rien ou si la cible est derrière un clone.', 10, 0, 0, 0, 0, 0, 1),
(114, 'Tour Rapide', 100, 1, 'Tour Rapide inflige des dégâts et annule les effets secondaires des capacités bloquantes, des capacités de pièges et de Vampigraine. Elle augmente aussi la vitesse d\'un cran.', 40, 0, 0, 0, 0, 0, 1),
(115, 'Toxik', 90, 8, 'Toxik empoisonne gravement la cible, celle-ci perdra 1/16 de ses PV maximum à la fin du tour durant lequel Toxik a été lancé. À la fin du tour suivant, la cible perdra 2/16 de ses PV maximum, puis 3/16 et ainsi de suite jusqu\'à ce qu\'elle tombe K.O. ou qu\'elle soit soignée. Si la cible alors atteinte par Toxik est switchée (sans être soignée), le décompte des PV perdus est réinitialisé à 1/16 lors de la fin du tour de son retour au combat, puis les PV perdus augmentent de la même façon que précédemment.', 10, 0, 0, 0, 0, 1, 0),
(116, 'Tricherie', 100, 16, 'Tricherie a une puissance de 95', 15, 1, 0, 0, 0, 0, 0),
(117, 'Tunnelier', 95, 9, 'Tunnelier, d\'une puissance de 80, a surtout pour avantage son taux de coups critiques élevé.', 10, 1, 0, 0, 0, 0, 0),
(118, 'Vampi-Poing', 100, 7, 'Un coup de poing qui draine l\'énergie. Convertit la moitié des dégâts infligés en PV pour le lanceur. Si la capacité n\'inflige qu\'1 PV de dégâts, le lanceur récupérera 1 PV.\r\n\r\nLes PV ne sont pas restaurés si la cible possède le talent Suintement ou est derrière un clone.', 10, 0, 0, 0, 0, 0, 1),
(119, 'Vampigraine', 90, 4, 'Vampigraine est une capacité qui permet de drainer de l\'énergie au Pokémon adverse. Le lanceur exécutant cette capacité lance une graine sur sa cible et lui absorbe à la fin de chaque tour 1/8e de ses PV. Si le lanceur est retiré, la capacité continue son effet vers le Pokémon remplacé, mais elle prend fin dès que la cible quitte le combat ou tombe K.O.. Si la cible a moins de 16 PV, Vampigraine ne draine que 1 PV du Pokémon adverse à chaque tour.\r\n\r\nCette capacité ne fonctionne pas contre les autres Pokémon de type Plante. Les capacités Buée Noire et Tour Rapide permet d\'arrêter l\'effet de Vampigraine. Lors des Combats Duo, les PV drainés à l\'adversaire ne sont redistribués que par le lanceur de la capacité ou le Pokémon qui le remplace. Si le lanceur tient l\'objet Grosseracine, Vampigraine draine 30% de plus, soit 16,25% des PV.', 10, 0, 0, 0, 0, 0, 1),
(120, 'Vampirisme', 100, 12, 'Vampirisme convertit la moitié des dégâts infligés en PV pour le lanceur. Si la capacité inflige 1 PV de dégâts, le lanceur récupérera 1 PV.\r\n\r\nLes PV ne sont pas restaurés si la cible possède le talent Suintement ou est derrière un clone.', 10, 0, 0, 0, 0, 0, 1),
(121, 'Vent Arrière', NULL, 10, 'Vent Arrière double la Vitesse du lanceur et de l\'ensemble des Pokémon de son équipe pendant 4 tours. ', 15, 0, 0, 0, 0, 0, 1),
(122, 'Vent Violent', 70, 10, 'Vent Violent, non content d\'être la plus puissante capacité de catégorie spéciale et de type Vol, a 30% de chances de rendre confus la cible, bien qu\'un clone soit immunisé à cet effet secondaire. Sa puissance est à 110.\r\n\r\nTout comme Fatal-Foudre, qui lui ressemble beaucoup, Vent Violent obtient 100% de précision sous la pluie et 50% sous le soleil.', 10, 1, 0, 0, 0, 0, 0),
(123, 'Vibraqua', 100, 3, 'Vibraqua inflige des dégâts et possède 20 % de chances de plonger la cible dans la confusion.', 20, 1, 0, 0, 0, 0, 0),
(124, 'Vibrobscur', 100, 16, 'Vibrobscur inflige des dégâts et possède 20 % de chances d\'apeurer la cible.', 15, 1, 0, 0, 0, 0, 0),
(125, 'Vitesse Extrême', 100, 1, 'Vitesse Extrême frappe en premier sans se soucier de la vitesse de la cible. En revanche, si la cible utilise également une capacité prioritaire, l\'ordre d\'attaque sera déterminé en fonction de la vitesse des deux lanceurs.\r\n\r\nSa priorité est à +2.', 5, 1, 0, 0, 0, 0, 0),
(126, 'Vive-Attaque', 100, 1, 'Vive-Attaque est une capacité très utile en début de partie, car apprise assez tôt ; surtout, sa priorité est de +1', 30, 1, 0, 0, 0, 0, 0),
(127, 'Voeu', 100, 1, 'Lors du tour où Vœu est lancé, le lanceur fait un vœu, sans plus d\'effets notables. À la fin du tour suivant, le Pokémon au combat se voit restaurer l\'équivalent de la moitié des PV maximum du lanceur.', 10, 0, 0, 0, 0, 0, 1),
(128, 'Vole-Force', 100, 4, 'La statistique d\'Attaque de la cible baisse, puis restaure les PV de l\'utilisateur de la même quantité que la statistique d\'Attaque effective de la cible avant l\'utilisation de Vole-Force.', 10, 0, 0, 0, 0, 0, 1);

-- --------------------------------------------------------

--
-- Structure de la table `attaquestatut`
--

CREATE TABLE `attaquestatut` (
  `id` int(11) NOT NULL,
  `attaqueId` int(11) DEFAULT NULL,
  `statutId` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `attaquestatut`
--

INSERT INTO `attaquestatut` (`id`, `attaqueId`, `statutId`) VALUES
(1, 49, 1),
(2, 53, 5),
(3, 88, 5),
(4, 104, 5),
(5, 115, 4);

-- --------------------------------------------------------

--
-- Structure de la table `climat`
--

CREATE TABLE `climat` (
  `id` int(11) NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `boostedTypeId` int(11) DEFAULT NULL,
  `nerfedTypeId` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `climat`
--

INSERT INTO `climat` (`id`, `name`, `boostedTypeId`, `nerfedTypeId`) VALUES
(1, 'Soleil', 2, 3),
(2, 'Pluie', 3, 2),
(3, 'Tempête de sable', 9, 6),
(4, 'Grêle', 6, 9);

-- --------------------------------------------------------

--
-- Structure de la table `item`
--

CREATE TABLE `item` (
  `id` int(11) NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `heal` tinyint(1) DEFAULT NULL,
  `buff` tinyint(1) DEFAULT NULL,
  `res` tinyint(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `item`
--

INSERT INTO `item` (`id`, `name`, `heal`, `buff`, `res`) VALUES
(1, 'Attaque +', 0, 1, 0),
(2, 'Défense +', 0, 1, 0),
(3, 'Atq. Spé. +', 0, 1, 0),
(4, 'Déf. Spé. +', 0, 1, 0),
(5, 'Vitesse +', 0, 1, 0),
(6, 'Précision +', 0, 1, 0),
(7, 'Eau Fraîche', 1, 0, 0),
(8, 'Super Potion', 1, 0, 0),
(9, 'Hyper Potion', 1, 0, 0),
(10, 'Potion Max', 1, 0, 0),
(11, 'Lait Meumeu', 1, 0, 0),
(12, 'Rappel', 0, 0, 1),
(13, 'Rappel Max', 0, 0, 1);

-- --------------------------------------------------------

--
-- Structure de la table `itembuff`
--

CREATE TABLE `itembuff` (
  `id` int(11) NOT NULL,
  `itemId` int(11) DEFAULT NULL,
  `StatBuff` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `itembuff`
--

INSERT INTO `itembuff` (`id`, `itemId`, `StatBuff`) VALUES
(1, 1, 'Att'),
(2, 2, 'Def'),
(3, 3, 'AttSpe'),
(4, 4, 'DefSpe'),
(5, 5, 'Speed'),
(6, 6, 'accuracy');

-- --------------------------------------------------------

--
-- Structure de la table `itemheal`
--

CREATE TABLE `itemheal` (
  `id` int(11) NOT NULL,
  `itemId` int(11) DEFAULT NULL,
  `PVHeal` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `itemheal`
--

INSERT INTO `itemheal` (`id`, `itemId`, `PVHeal`) VALUES
(1, 7, 130),
(2, 8, 60),
(3, 9, 120),
(4, 10, 500),
(5, 11, 100);

-- --------------------------------------------------------

--
-- Structure de la table `itemres`
--

CREATE TABLE `itemres` (
  `id` int(11) NOT NULL,
  `itemId` int(11) DEFAULT NULL,
  `PV` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `itemres`
--

INSERT INTO `itemres` (`id`, `itemId`, `PV`) VALUES
(1, 12, 50),
(2, 13, 100);

-- --------------------------------------------------------

--
-- Structure de la table `nature`
--

CREATE TABLE `nature` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `stat_buff` varchar(255) DEFAULT NULL,
  `stat_nerf` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `nature`
--

INSERT INTO `nature` (`id`, `name`, `stat_buff`, `stat_nerf`) VALUES
(1, 'Assuré', 'Def', 'Att'),
(2, 'Bizarre', NULL, NULL),
(3, 'Brave', 'Att', 'Speed'),
(4, 'Calme', 'DefSpe', 'Att'),
(5, 'Discret', 'AttSpe', 'Speed'),
(6, 'Docile', NULL, NULL),
(7, 'Doux', 'AttSpe', 'Def'),
(8, 'Foufou', 'AttSpe', 'DefSpe'),
(9, 'Gentil', 'DefSpe', 'Def'),
(10, 'Hardi', NULL, NULL),
(11, 'Jovial', 'Speed', 'AttSpe'),
(12, 'Lâche', 'Def', 'DefSpe'),
(13, 'Malin', 'Def', 'AttSpe'),
(14, 'Malpoli', 'DefSpe', 'Speed'),
(15, 'Mauvais', 'Att', 'DefSpe'),
(16, 'Modeste', 'AttSpe', 'Att'),
(17, 'Naïf', 'Speed', 'DefSpe'),
(18, 'Pressé', 'Speed', 'Def'),
(19, 'Prudent', 'DefSpe', 'AttSpe'),
(20, 'Pudique', NULL, NULL),
(21, 'Relax', 'Def', 'Speed'),
(22, 'Rigide', 'Att', 'AttSpe'),
(23, 'Sérieux', NULL, NULL),
(24, 'Solo', 'Att', 'Def'),
(25, 'Timide', 'Speed', 'Att');

-- --------------------------------------------------------

--
-- Structure de la table `pokemon`
--

CREATE TABLE `pokemon` (
  `id` int(11) NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `sprite` varchar(255) DEFAULT NULL,
  `spriteDos` varchar(255) DEFAULT NULL,
  `typeId` int(11) DEFAULT NULL,
  `typeId2` int(11) DEFAULT NULL,
  `natureId` int(11) NOT NULL,
  `PV` int(11) DEFAULT NULL,
  `Att` int(11) DEFAULT NULL,
  `Def` int(11) DEFAULT NULL,
  `AttSpe` int(11) DEFAULT NULL,
  `DefSpe` int(11) DEFAULT NULL,
  `Speed` int(11) DEFAULT NULL,
  `accuracy` int(11) NOT NULL,
  `AttaqueId1` int(11) DEFAULT NULL,
  `AttaqueId2` int(11) DEFAULT NULL,
  `AttaqueId3` int(11) DEFAULT NULL,
  `AttaqueId4` int(11) DEFAULT NULL,
  `Poids` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `pokemon`
--

INSERT INTO `pokemon` (`id`, `name`, `sprite`, `spriteDos`, `typeId`, `typeId2`, `natureId`, `PV`, `Att`, `Def`, `AttSpe`, `DefSpe`, `Speed`, `accuracy`, `AttaqueId1`, `AttaqueId2`, `AttaqueId3`, `AttaqueId4`, `Poids`) VALUES
(1, 'Aéromite', 'Aeromite.gif', 'Aeromite.png', 12, 8, 25, 70, 65, 60, 90, 75, 90, 0, 73, 88, 16, 14, 13),
(2, 'Akwakwak', 'Akwakwak.gif', 'Akwakwak.png', 3, NULL, 16, 80, 82, 78, 95, 80, 85, 0, 34, 54, 62, 93, 76),
(3, 'Alakazam', 'Alakazam.gif', 'Alakazam.png', 11, NULL, 25, 55, 50, 45, 135, 95, 120, 0, 92, 45, 102, 10, 48),
(4, 'Amonistar', 'Amonistar.gif', 'Amonistar.png', 13, 3, 25, 70, 60, 125, 115, 70, 55, 0, 47, 54, 62, 93, 35),
(5, 'Aquiali', 'Aquali.gif', 'Aquali.png', 3, NULL, 4, 130, 65, 60, 110, 95, 65, 0, 40, 127, 1, 62, 29),
(6, 'Arbok', 'Arbok.gif', 'Arbok.png', 8, NULL, 22, 60, 85, 69, 65, 79, 80, 0, 38, 44, 28, 55, 65),
(7, 'Arcanin', 'Arcanin.gif', 'Arcanin.png', 2, NULL, 22, 90, 110, 80, 100, 80, 95, 0, 17, 125, 41, 6, 155),
(8, 'Artikodin', 'Artikodin.gif', 'Artikodin.png', 6, 10, 16, 90, 85, 100, 95, 125, 85, 0, 4, 64, 51, 2, 55),
(9, 'Canarticho', 'Canarticho.gif', 'Canarticho.png', 1, 10, 22, 52, 90, 55, 58, 62, 60, 0, 33, 94, 59, 126, 15),
(10, 'Colossinge', 'Colossinge.gif', 'Colossinge.png', 7, NULL, 11, 65, 105, 60, 60, 70, 95, 0, 25, 35, 58, 110, 32),
(11, 'Crustabri', 'Crustabri.gif', 'Crustabri.png', 3, 6, 11, 50, 95, 180, 85, 45, 70, 0, 75, 47, 105, 114, 132),
(12, 'Dardagnan', 'Dardagnan.gif', 'Dardagnan.png', 12, 8, 11, 65, 80, 40, 45, 80, 75, 0, 76, 43, 121, 81, 30),
(13, 'Dodrio', 'Dodrio.gif', 'Dodrio.png', 1, 10, 11, 60, 110, 70, 60, 60, 110, 0, 94, 99, 77, 100, 85),
(14, 'Dracaufeu', 'Dracaufeu.gif', 'Dracaufeu.png', 2, 10, 11, 78, 84, 78, 109, 85, 100, 0, 32, 26, 17, 110, 90),
(15, 'Dracolosse', 'Dracolosse.gif', 'Dracolosse.png', 15, 10, 22, 91, 134, 95, 100, 100, 80, 0, 26, 125, 85, 110, 210),
(16, 'Ectoplasma', 'Ectoplasma.gif', 'Ectoplasma.png', 14, 8, 25, 60, 65, 60, 130, 75, 110, 0, 10, 30, 45, 113, 40),
(17, 'Electhor', 'Electhor.gif', 'Electhor.png', 5, 10, 25, 90, 90, 85, 125, 90, 100, 0, 29, 93, 18, 4, 52),
(18, 'Electrode', 'Electrode.gif', 'Electrode.png', 5, NULL, 16, 60, 50, 70, 80, 80, 150, 0, 25, 35, 58, 110, 66),
(19, 'Elekable', 'Elekable.gif', 'Elekable.png', 5, NULL, 17, 75, 123, 67, 95, 85, 95, 0, 112, 21, 95, 93, 138),
(20, 'Empiflor', 'Empiflor.gif', 'Empiflor.png', 4, 8, 16, 80, 105, 65, 100, 70, 70, 0, 61, 14, 9, 88, 15),
(21, 'Excelangue', 'Excelangue.gif', 'Excelangue.png', 1, NULL, 13, 90, 55, 75, 60, 75, 30, 0, 127, 1, 82, 100, 65),
(22, 'Feunard', 'Feunard.gif', 'Feunard.png', 2, NULL, 25, 73, 76, 75, 81, 100, 100, 0, 106, 37, 61, 93, 19),
(23, 'Flagadoss', 'Flagadoss.gif', 'Flagadoss.png', 3, 11, 1, 95, 75, 110, 100, 80, 30, 0, 40, 62, 74, 115, 78),
(24, 'Florizarre', 'Florizarre.gif', 'Florizarre.png', 4, 88, 1, 80, 82, 83, 100, 100, 80, 0, 119, 115, 109, 71, 100),
(25, 'Galopa', 'Galopa.gif', 'Galopa.png', 2, NULL, 11, 65, 100, 70, 80, 80, 105, 0, 17, 41, 6, 49, 95),
(26, 'Grodoudou', 'Grodoudou.gif', 'Grodoudou.png', 1, 18, 25, 140, 70, 45, 75, 50, 45, 0, 80, 70, 42, 37, 12),
(27, 'Grolem', 'Grolem.gif', 'Grolem.png', 9, 13, 22, 80, 120, 130, 55, 65, 45, 0, 80, 110, 58, 46, 300),
(28, 'Grotadmorv', 'Grotadmorv.gif', 'Grotadmorv.png', 8, NULL, 22, 105, 105, 75, 65, 100, 50, 0, 38, 72, 86, 84, 30),
(29, 'Hypnomade', 'Hypnomade.gif', 'Hypnomade.png', 11, NULL, 4, 85, 73, 70, 73, 115, 67, 0, 127, 1, 115, 116, 75),
(30, 'Hyporoi', 'Hyporoi.gif', 'Hyporoi.png', 3, 15, 16, 75, 95, 95, 95, 95, 85, 0, 54, 36, 62, 107, 152),
(31, 'Insecateur', 'Insecateur.gif', 'Insecateur.png', 12, 10, 11, 70, 110, 80, 55, 80, 105, 0, 35, 7, 20, 100, 56),
(32, 'Kabutops', 'Kabutops.gif', 'Kabutops.png', 13, 3, 22, 60, 115, 105, 65, 70, 80, 0, 58, 3, 33, 108, 40),
(33, 'Kangourex', 'Kangourex.gif', 'Kangourex.png', 1, NULL, 22, 105, 95, 80, 40, 80, 90, 0, 13, 31, 110, 28, 80),
(34, 'Kicklee', 'Kicklee.gif', 'Kicklee.png', 7, NULL, 11, 50, 120, 53, 35, 110, 87, 0, 100, 78, 52, 23, 50),
(35, 'Krabboss', 'Krabboss.gif', 'Krabboss.png', 3, NULL, 11, 55, 130, 115, 50, 50, 75, 0, 33, 3, 100, 56, 60),
(36, 'Lamantine', 'Lamantine.gif', 'Lamantine.png', 3, 6, 4, 90, 70, 80, 70, 97, 70, 0, 101, 98, 34, 97, 120),
(37, 'Leveinard', 'Leveinard.gif', 'Leveinard.png', 1, NULL, 1, 250, 5, 5, 35, 105, 50, 0, 50, 115, 80, 39, 34),
(38, 'Leviator', 'Leviator.gif', 'Leviator.png', 3, 10, 11, 95, 125, 79, 60, 100, 81, 0, 32, 68, 110, 24, 235),
(39, 'Lippoutou', 'Lippoutou.gif', 'Lippoutou.png', 6, 11, 25, 65, 50, 35, 115, 95, 95, 0, 62, 92, 45, 53, 40),
(40, 'Lokhlass', 'Lokhlass.gif', 'Lokhlass.png', 3, 6, 16, 130, 85, 80, 85, 95, 60, 0, 64, 54, 62, 93, 220),
(41, 'Mackogneur', 'Mackogneur.gif', 'Mackogneur.png', 7, NULL, 22, 90, 130, 80, 65, 85, 55, 0, 25, 100, 48, 79, 130),
(42, 'Magmar', 'Magmar.gif', 'Magmar.png', 2, NULL, 25, 65, 95, 57, 100, 85, 93, 0, 37, 112, 45, 93, 45),
(43, 'Magnéton', 'Magneton.gif', 'Magneton.png', 5, 17, 25, 50, 60, 95, 120, 70, 70, 0, 21, 112, 63, 93, 60),
(44, 'Mélodelfe', 'Melodelfe.gif', 'Melodelfe.png', 18, NULL, 1, 95, 70, 73, 85, 90, 60, 0, 83, 90, 39, 80, 40),
(45, 'Mew', 'Mew.gif', 'Mew.png', 11, NULL, 16, 100, 100, 100, 100, 100, 100, 0, 66, 92, 37, 87, 4),
(46, 'Mewtwo', 'Mewtwo.gif', 'Mewtwo.png', 11, NULL, 25, 106, 110, 90, 154, 90, 130, 0, 92, 37, 45, 10, 122),
(47, 'Nidoking', 'Nidoking.gif', 'Nidoking.png', 8, 9, 25, 81, 102, 77, 85, 75, 85, 0, 111, 30, 62, 24, 62),
(48, 'Nidoqueen', 'Nidoqueen.gif', 'Nidoqueen.png', 8, 9, 1, 90, 92, 87, 75, 85, 76, 0, 111, 76, 62, 30, 60),
(49, 'Noadkoko', 'Noadkoko.gif', 'Noadkoko.png', 4, 11, 16, 95, 95, 85, 125, 75, 55, 0, 61, 22, 93, 88, 120),
(50, 'Nosferalto', 'Nosferalto.gif', 'Nosferalto.png', 8, 10, 19, 75, 80, 70, 65, 75, 90, 0, 4, 2, 94, 115, 55),
(51, 'Onix', 'Onix.gif', 'Onix.png', 9, 13, 11, 35, 45, 160, 30, 45, 70, 0, 80, 15, 110, 46, 210),
(52, 'Ossatueur', 'Ossatueur.gif', 'Ossatueur.png', 9, NULL, 22, 60, 80, 110, 50, 80, 45, 0, 110, 100, 33, 24, 45),
(53, 'Papilusion', 'Papilusion.gif', 'Papilusion.png', 10, 12, 25, 60, 45, 50, 90, 80, 70, 0, 73, 88, 16, 57, 32),
(54, 'Parasect', 'Parasect.gif', 'Parasect.png', 4, 12, 19, 60, 95, 80, 60, 80, 30, 0, 120, 104, 100, 109, 30),
(55, 'Persian', 'Persian.gif', 'Persian.png', 1, NULL, 25, 65, 70, 60, 65, 65, 115, 0, 66, 70, 93, 123, 32),
(56, 'Poissoroy', 'Poissoroy.gif', 'Poissoroy.png', 3, NULL, 22, 80, 92, 65, 65, 80, 68, 0, 19, 100, 117, 69, 39),
(57, 'Porygon', 'Porygon.gif', 'Porygon.png', 1, NULL, 25, 65, 60, 70, 85, 75, 40, 0, 112, 62, 102, 27, 37),
(58, 'Ptéra', 'Ptera.gif', 'Ptera.png', 10, 13, 11, 80, 105, 65, 60, 75, 130, 0, 58, 110, 89, 55, 59),
(59, 'Pyroli', 'Pyroli.gif', 'Pyroli.png', 2, NULL, 22, 65, 130, 60, 95, 110, 65, 0, 17, 108, 126, 31, 25),
(60, 'Rafflésia', 'Rafflesia.gif', 'Rafflesia.png', 4, 8, 1, 75, 80, 85, 100, 90, 50, 0, 14, 128, 88, 93, 19),
(61, 'Raichu', 'Raichu.gif', 'Raichu.png', 5, NULL, 25, 60, 90, 55, 90, 80, 110, 0, 66, 112, 62, 93, 30),
(62, 'Rapasdepic', 'Rapasdepic.gif', 'Rapasdepic.png', 1, 10, 11, 65, 90, 65, 61, 61, 100, 0, 11, 31, 117, 35, 38),
(63, 'Rattatac', 'Rattatac.gif', 'Rattatac.png', 1, NULL, 11, 55, 81, 60, 50, 70, 97, 0, 48, 28, 1, 35, 19),
(64, 'Rhinoféros', 'Rhinoferos.gif', 'Rhinoferos.png', 9, 13, 22, 105, 130, 120, 45, 45, 40, 0, 80, 110, 15, 33, 120),
(65, 'Ronflex', 'Ronflex.gif', 'Ronflex.png', 1, NULL, 19, 160, 110, 65, 65, 110, 30, 0, 67, 99, 97, 12, 460),
(66, 'Roucarnage', 'Roucarnage.gif', 'Roucarnage.png', 1, 10, 25, 83, 80, 75, 70, 70, 101, 0, 122, 18, 4, 35, 40),
(67, 'Sablaireau', 'Sablaireau.gif', 'Sablaireau.png', 9, NULL, 22, 75, 100, 110, 45, 55, 65, 0, 110, 33, 100, 58, 30),
(68, 'Scarabrute', 'Scarabrute.gif', 'Scarabrute.png', 12, NULL, 11, 65, 125, 100, 55, 70, 85, 0, 33, 81, 110, 58, 55),
(69, 'Smogogo', 'Smogogo.gif', 'Smogogo.png', 8, NULL, 1, 65, 90, 120, 85, 70, 60, 0, 14, 49, 8, 76, 10),
(70, 'Staross', 'Staross.gif', 'Staross.png', 3, 11, 25, 60, 75, 85, 100, 85, 110, 0, 40, 115, 102, 114, 80),
(71, 'Sulfura', 'Sulfura.gif', 'Sulfura.png', 2, 10, 25, 90, 100, 90, 125, 85, 90, 0, 24, 4, 4, 60, 60),
(72, 'Tartard', 'Tartard.gif', 'Tartard.png', 3, 7, 21, 90, 95, 95, 70, 90, 70, 0, 40, 97, 12, 91, 54),
(73, 'Tauros', 'Tauros.gif', 'Tauros.png', 1, NULL, 17, 75, 100, 95, 40, 70, 110, 0, 82, 37, 96, 110, 89),
(74, 'Tentacruel', 'Tentacruel.gif', 'Tentacruel.png', 3, 8, 4, 80, 70, 65, 80, 120, 100, 0, 40, 76, 114, 1, 55),
(75, 'Tortank', 'Tortank.gif', 'Tortank.png', 3, NULL, 16, 79, 83, 100, 85, 105, 78, 0, 123, 124, 5, 62, 86),
(76, 'Triopikeur', 'Triopikeur.gif', 'Triopikeur.png', 9, NULL, 11, 35, 100, 50, 50, 70, 120, 0, 110, 58, 103, 80, 34),
(77, 'Tygnon', 'Tygnon.gif', 'Tygnon.png', 7, NULL, 22, 50, 105, 79, 35, 110, 76, 0, 118, 65, 86, 114, 50),
(78, 'Voltali', 'Voltali.gif', 'Voltali.png', 5, NULL, 25, 65, 65, 60, 110, 95, 130, 0, 112, 21, 93, 10, 25);

-- --------------------------------------------------------

--
-- Structure de la table `statuts`
--

CREATE TABLE `statuts` (
  `id` int(11) NOT NULL,
  `name` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `statuts`
--

INSERT INTO `statuts` (`id`, `name`) VALUES
(1, 'Brûlure'),
(2, 'Gel'),
(3, 'Paralysie'),
(4, 'Empoisonnement'),
(5, 'Sommeil');

-- --------------------------------------------------------

--
-- Structure de la table `types`
--

CREATE TABLE `types` (
  `id` int(11) NOT NULL,
  `name` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `types`
--

INSERT INTO `types` (`id`, `name`) VALUES
(1, 'Normal'),
(2, 'Feu'),
(3, 'Eau'),
(4, 'Plante'),
(5, 'Electrik'),
(6, 'Glace'),
(7, 'Combat'),
(8, 'Poison'),
(9, 'Sol'),
(10, 'Vol'),
(11, 'Psy'),
(12, 'Insecte'),
(13, 'Roche'),
(14, 'Spectre'),
(15, 'Dragon'),
(16, 'Tenebre'),
(17, 'Acier'),
(18, 'Fee');

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `attaqueautres`
--
ALTER TABLE `attaqueautres`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `attaquebuff`
--
ALTER TABLE `attaquebuff`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `attaqueclimat`
--
ALTER TABLE `attaqueclimat`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `attaqueheal`
--
ALTER TABLE `attaqueheal`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `attaqueoffensive`
--
ALTER TABLE `attaqueoffensive`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `attaques`
--
ALTER TABLE `attaques`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `attaquestatut`
--
ALTER TABLE `attaquestatut`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `climat`
--
ALTER TABLE `climat`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `item`
--
ALTER TABLE `item`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `itembuff`
--
ALTER TABLE `itembuff`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `itemheal`
--
ALTER TABLE `itemheal`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `itemres`
--
ALTER TABLE `itemres`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `nature`
--
ALTER TABLE `nature`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `pokemon`
--
ALTER TABLE `pokemon`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `statuts`
--
ALTER TABLE `statuts`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `types`
--
ALTER TABLE `types`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `attaqueautres`
--
ALTER TABLE `attaqueautres`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=50;

--
-- AUTO_INCREMENT pour la table `attaquebuff`
--
ALTER TABLE `attaquebuff`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=30;

--
-- AUTO_INCREMENT pour la table `attaqueclimat`
--
ALTER TABLE `attaqueclimat`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT pour la table `attaqueheal`
--
ALTER TABLE `attaqueheal`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT pour la table `attaqueoffensive`
--
ALTER TABLE `attaqueoffensive`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=58;

--
-- AUTO_INCREMENT pour la table `attaques`
--
ALTER TABLE `attaques`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=129;

--
-- AUTO_INCREMENT pour la table `attaquestatut`
--
ALTER TABLE `attaquestatut`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT pour la table `climat`
--
ALTER TABLE `climat`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT pour la table `item`
--
ALTER TABLE `item`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT pour la table `itembuff`
--
ALTER TABLE `itembuff`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT pour la table `itemheal`
--
ALTER TABLE `itemheal`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT pour la table `itemres`
--
ALTER TABLE `itemres`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT pour la table `nature`
--
ALTER TABLE `nature`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;

--
-- AUTO_INCREMENT pour la table `pokemon`
--
ALTER TABLE `pokemon`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=79;

--
-- AUTO_INCREMENT pour la table `statuts`
--
ALTER TABLE `statuts`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT pour la table `types`
--
ALTER TABLE `types`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

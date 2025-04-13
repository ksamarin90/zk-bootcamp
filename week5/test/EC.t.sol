// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;

import {Test, console} from "forge-std/Test.sol";
import {EC, ECPoint} from "../src/EC.sol";

contract ECTest is Test {
    EC public ec;

    function setUp() public {
        ec = new EC();
    }

    function test_rationalAdd() external {
        {
            // "12" + 97 = 109
            ECPoint memory A = ECPoint(
                // Malformed x value
                17108685722251241369314020928988529881027530433467445791267465866135602972754,
                20666112440056908034039013737427066139426903072479162670940363761207457724060
            );
            ECPoint memory B = ECPoint(
                5060549300900576002438537256617533285303175982423725591354110924059445776301,
                21432174468722130278193150581548751041331147035316420546597625954751666563889
            );
            vm.expectRevert("Invalid EC Points");
            ec.rationalAdd(A, B, 109, 1);
        }
        {
            // 13 + 97 != 109
            ECPoint memory A = ECPoint(
                2672242651313367459976336264061690128665099451055893690004467838496751824703,
                18247534626997477790812670345925575171672701304065784723769023620148097699216
            );
            ECPoint memory B = ECPoint(
                5060549300900576002438537256617533285303175982423725591354110924059445776301,
                21432174468722130278193150581548751041331147035316420546597625954751666563889
            );

            assertFalse(ec.rationalAdd(A, B, 109, 1));
        }
        {
            // 12 + 97 = 109
            ECPoint memory A = ECPoint(
                17108685722251241369314020928988529881027530433467445791267465866135602972753,
                20666112440056908034039013737427066139426903072479162670940363761207457724060
            );
            ECPoint memory B = ECPoint(
                5060549300900576002438537256617533285303175982423725591354110924059445776301,
                21432174468722130278193150581548751041331147035316420546597625954751666563889
            );

            assertTrue(ec.rationalAdd(A, B, 109, 1));
        }
        {
            // 12/47 + 33/48 = 709/752
            ECPoint memory A = ECPoint(
                12128416201425586622560549136756833541677226724755842857149169194444003774891,
                10716236668643904157825611563182236788643420177660645656726006020062202748022
            );
            ECPoint memory B = ECPoint(
                16099420920581702255175293724868659223567756114032025470083056370421188271727,
                9750807591715237082474515017943621170174530282279931935262470395760951492455
            );

            assertTrue(ec.rationalAdd(A, B, 709, 752));
        }
    }

    function test_matmul() external {
        uint256[] memory matrix = new uint256[](9);
        matrix[0] = 1;
        matrix[1] = 2;
        matrix[2] = 3;
        matrix[3] = 4;
        matrix[4] = 5;
        matrix[5] = 6;
        matrix[6] = 7;
        matrix[7] = 8;
        matrix[8] = 9;

        uint256 n = 3;

        ECPoint[] memory s = new ECPoint[](3);
        s[0] = ECPoint(
            17108685722251241369314020928988529881027530433467445791267465866135602972753,
            20666112440056908034039013737427066139426903072479162670940363761207457724060
        );
        s[1] = ECPoint(
            12643418736033227053786352010911706350519409749146221098915102879679320422546,
            20244910942408978007550006931066140611657597349862739175933913066040413145521
        );
        s[2] = ECPoint(
            13940766438396802022003403700150119103921439873158775302201999840306601026555,
            20366854387609749451649589446643328667334616581983267447585608088473228416457
        );

        uint256[] memory o = new uint256[](3);
        o[0] = 141;
        o[1] = 339;
        o[2] = 537;

        assertTrue(ec.matmul(matrix, n, s, o));

        matrix[8] = 100500;

        assertFalse(ec.matmul(matrix, n, s, o));

        vm.expectRevert("Incorrect input data");
        ec.matmul(matrix, 2, s, o);
        vm.expectRevert("Incorrect input data");
        ec.matmul(new uint256[](8), n, s, o);
        vm.expectRevert("Incorrect input data");
        ec.matmul(matrix, n, new ECPoint[](2), o);
        vm.expectRevert("Incorrect input data");
        ec.matmul(new uint256[](8), n, s, new uint256[](2));
    }
}

// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;

struct ECPoint1 {
    uint256 x;
    uint256 y;
}

struct ECPoint2 {
    uint256[2] x;
    uint256[2] y;
}

contract EC {
    uint256 constant CURVE_ORDER = 21888242871839275222246405745257275088548364400416034343698204186575808495617;
    uint256 constant FIELD_MODULUS = 21888242871839275222246405745257275088696311157297823662689037894645226208583;

    ECPoint1 G1 = ECPoint1(1, 2);

    ECPoint1 ALPHA_1 = ECPoint1(
        7005788933776043886113595351870582064790836204699225509625672914853557488211,
        251174205643241124756207588463609744388781834588134075745959492296673029679
    );
    ECPoint2 BETA_2 = ECPoint2(
        [
            11250017886832013765169534486309099260111359876823821868580101161001083387095,
            6795553187396938009242954317676878823221820017911755786061734031710469155973
        ],
        [
            17817227677413981972537966088089842374464768902165360954427360267005402539103,
            11122293121052968686665069059017126703228920907390971117524055967010646754578
        ]
    );
    ECPoint2 GAMMA_2 = ECPoint2(
        [
            16577408282369182483487480469643897259471913482788194293282274448197032142798,
            21490742268769407614733184184484206579974779934991894568564503113160034400833
        ],
        [
            7305780354224297507702020492982526780892929211617347875619393179684229322049,
            14319333942550957887183262837232902362778631271894372984524619053056496956082
        ]
    );
    ECPoint2 DELTA_2 = ECPoint2(
        [
            16510881685709123496626165154620052396783760295393338639709553733744655001043,
            3507970681433487728342275806025499981249751236893088393424903349335004610958
        ],
        [
            19991476996943068015355572683572799684536924145965655186227512779672417059563,
            21189682753391890686949110833744962537073772786274572136201368677556088732025
        ]
    );

    function isBalanced(
        ECPoint1 calldata A1,
        ECPoint2 calldata B2,
        ECPoint1 calldata C1,
        uint256 x1,
        uint256 x2,
        uint256 x3
    ) external view returns (bool) {
        ECPoint1 memory X_1 = _getX_1(x1, x2, x3);
        ECPoint1 memory negA1 = ECPoint1(A1.x, FIELD_MODULUS - A1.y);

        uint256[24] memory input = [
            negA1.x,
            negA1.y,
            B2.x[1],
            B2.x[0],
            B2.y[1],
            B2.y[0],
            ALPHA_1.x,
            ALPHA_1.y,
            BETA_2.x[1],
            BETA_2.x[0],
            BETA_2.y[1],
            BETA_2.y[0],
            X_1.x,
            X_1.y,
            GAMMA_2.x[1],
            GAMMA_2.x[0],
            GAMMA_2.y[1],
            GAMMA_2.y[0],
            C1.x,
            C1.y,
            DELTA_2.x[1],
            DELTA_2.x[0],
            DELTA_2.y[1],
            DELTA_2.y[0]
        ];

        (bool success, bytes memory res) = address(0x08).staticcall(abi.encode(input));

        require(success, "Pairing failed");
        uint256 result = abi.decode(res, (uint256));
        return result == 1;
    }

    function _addPoints(ECPoint1 memory A, ECPoint1 memory B) internal view returns (ECPoint1 memory) {
        (bool success, bytes memory result) = address(0x06).staticcall(abi.encode(A.x, A.y, B.x, B.y));
        require(success, "Invalid EC Points");
        (uint256 x, uint256 y) = abi.decode(result, (uint256, uint256));
        return ECPoint1(x, y);
    }

    function _scalarMul(ECPoint1 memory point, uint256 scalar) internal view returns (ECPoint1 memory) {
        (bool success, bytes memory result) = address(0x07).staticcall(abi.encode(point.x, point.y, scalar));
        require(success, "C point calculation failed");
        (uint256 x, uint256 y) = abi.decode(result, (uint256, uint256));
        return ECPoint1(x, y);
    }

    function _getX_1(uint256 x1, uint256 x2, uint256 x3) internal view returns (ECPoint1 memory result) {
        ECPoint1 memory X1 = _scalarMul(G1, x1);
        ECPoint1 memory X2 = _scalarMul(G1, x2);
        ECPoint1 memory X3 = _scalarMul(G1, x3);
        result = X1;
        result = _addPoints(result, X2);
        result = _addPoints(result, X3);
    }
}

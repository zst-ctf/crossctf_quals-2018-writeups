import binascii
from kryptonite import Cipher

key = bytes.fromhex('b5a7f63abb94d07d1a6445c36c07c7e8327fe61b1647e391b4c7edae5de57a3d'[-32:])
key = Cipher.generate_key()
cipher = Cipher(key)
in_txt = bytes.fromhex("b433c1d04f324ea36b7a24e57923b481871831c727b41dc25e54dc49ad3970e59775b7f3543c6fc495951146ac821523afef0bc1d144fae68dc01c58513733880ac79157d3056543ea0ac4bd0b2265d359abb225959aac0a2087b2775cf70388d9427b66e461ff77db6d8900b39e2323a9111de7e49969637c839cd35ca3695afa57d279547df3565ea8c2c1dad017bc4325f5154563544a585abbf5f156e9c29360a6e9ee1f825c8f438be956e7a254e537bd69b254a6893c26a3992aa459772820032e85dcee2a40e8edfa41cdbe3ac5ed54382addebe1a42be0112a0b20c3d78d972d4e46d4cea6cd39046737dc32cd9b07b028aed4123ca30e556dc180f0b8340e0053a20a294c9346e09cc0f9d52a5a0f8bb39eeba8a82c3e4d127c8188f68baee65d86ae6448356f7724d2369ac27b1b52d29e6bce4b576c563270198139ad942b9254b5a21338072e3625bf5f82c2bee457206ee2543aa66acfbfe78b66a36c516dcbcb34af21d1bc7a76f089014a1b6b41fd3dc8cadd16efbfd0b7f5c186d34524de3c63fe8eabc4fb80f74e94107e39c66294ab03715ec2ab58b65d733501555a6c44062652f2d79a7b0ab60d5d29e75643593c7d48ecd56cbcc355ed674ce93d4a41e0bc0b54f5f81b4ba2e2b5dab4f404b6ce6b6cc96476dabe19e7e072c12b832afb3811e7e3b7c53b37ea9002b8ff04f33cf9f8b6b72be01240aedddd22cdd9f748095a6536d14dc05555e3b8fd6c989394da19da7a24f590ee4c77f0c1a984ad7c87cf0e241407ef7ee7c4810a1990d818835fe40f14298c62867d31574e2f06bf5943c4e057fa39fb6e3c32e4bed467626a021aa6dbf71a6437dc3dc112efa97b827547c7a4708ca730c20e924a6e12f4cbf7bb9bcfa310fe3c2c0d05a2e2cf6c0175d757f796dfd61326d41bc9b07fc819e154cc2c9ad450b7f8547d5539fb3ad9d10323bd07167944e20b48343c99aa9784f7102594c666a5157d6b54c6c0e32777c8b203f9135742fdf21f83509f5967d595e0fcd826982c4e961b4a9de53dec194ebe4ab99c0c9159d5ae35ee56a58e2805c39042586770eb8895863b1be6c873a6abd93c95deb4272cf0b421afc430f843bde27a12189d9cca9c9c36298af220ce4a42a5da1f8a96cb463115b3df9133cb7e0ef7fb7cc84c463f509dc6b416874d303f72a21ac5b7432d8eb05037e20710e33c9259ca8fb13ab9f848292022a40db12cfdb59ff2e32f95ff042d5bb894d3faf91117881d518eaf6e80b75df87ec83bf3a780470e83966abb90e91634fe240909c378fe6daed3ab914516bacefbb88088896c0ec3f5e5623731852e6ddedefd3854d6cb50defe896be25cf0aded5cf7f06a225ddd98ab0ba098f22ff59500e5b371faa40c234cdf0ca90b9a8116a975e2d43d5f7edd4478e3418c27b71ac2d351318b2a098f35db5ec337051461fce72d652e2b4f6add01715905545029ba8d855ddf30ca55d22cfb906f2c95cbb1f2fda1929db2aa180f5b8d63b77e2ce66be53bca5acf397477cea147ccf0f7c920b740c33fd05c14214d8281c4fe9d279bfadd08a998832142fc030f0fd328892264ad8218d1c20f47e7dde9717ea2b4d5382e93669fc094782d10e4a7a2f146de69571e87bd2ad05478043524654721a4179ed97249f62699b385f19b90421fd8cff4ba199d219b7304c15950cf1a50fefbf263aaf64078fa1e6f5d6e16ca6e191b02ae649fa66ad78f9e3289d70e2da26cdb1da7d2355f2e2cbc0af267ca4b99ada9dcf0c612e94a655f959009dfea616c12218e25cb256d63491364f6ba3809cdbe2ed036ab3bb35848fcc0444e63eaeb5cee101b382d3eb49dc43d59bb6590b65691eda9498119369760a1c84eb9c60b32425c27fa7150566fe8cfaae61fdd1258e1e0179a0dbe60754234f4526e64515321a006ba5cf7556479d1e986aaecd83c86f77886edd29a5bf3f4f8e1ffbc319d7f624fa21ccc5b483f448febe6870e1a9cf6ca7df588a610e7a4d999b84ce6e642678fe7c67ef427f16f7e7178bb1eadb18d027ee2f0cd7ec028b2bb4498661cad81ccf36c4be17da590b5ad02d109316bcceeff134ff3d8a3db7a2ea42ebc3042c6be0600e2b01ec434bb2431c43a0fb094c2a2684e54c1d6a323bb003f99a64691638906146f938ecdd0ae674d7b180d2c20adf7be6fe818a5eb970159aa9df93584cc3aa14973b925a5723e5a47bfc99d1fec97065b07d4e972b6e0befce662a87b7888a3856c8ea1e42da3f2fd35ce7b02361c3b93b92553c8804a8670b24cb835a6b05562b9c463d064515ec496b7bbd329c95248bb21b5b9fcf851cbecebf69328d1ef6bc719b631bde7b3d25798421e2941b86da13ae501ec5b02385bb7db275244242fa9ceb72f1432e4e1b74c44d926c2741357e3f33c2777f7f39104ec33d30c60eae42ba48df406b2f258aeefb50c20fbac6aa2ef2758ff8bbaf1b3ea9ed8b2eabeb51034943328cad23cee1469f50bf70c7169a86cac4c0d09e162514fc3fac1271b31925d95305a3d77ebe8193405a26142cf79c9e23fcdc3db7b18787a31d56d0d72356ab4fb84325533804cd85c9599dff38a544765a49d9d48f4e403bf69a032fcff7f782a805c97d5a50d0a91c6409954a32f30bab267e4d511721fcdc1ac29ef1811b5de824cfd01c54b2bf5cb107aae10938cd3bd263da7f06925fed78f2ee0d425a36a6916d96b97829746463c057d034a79bd311fc7daeee4785aa8263b1d8bd4f55390157037d562ee156a5486dce168bf2ccb4ddcfeab734491b26245654c4719ace87f9f54ba")
out_txt = cipher.encrypt(in_txt)

hexstring = binascii.hexlify(out_txt)
print(hexstring)

## Descripción
Can you find the flag? [shark2.pcapng](https://mercury.picoctf.net/static/7b8e53329b34946177a9b5f2860a0292/shark2.pcapng).

## Pistas
- Did you really find _the_ flag?
- Look for traffic that seems suspicious.

## Solución
- Pra resolver este reto, se nos da un archivo de paquetes de trafico de red.
- Al analizar el protocolo TCP, parece que hay muchas solicitudes a un punto final `/flag`. Cada solicitud muestra una bandera diferente, por lo que deben ser una distracción. Para comprobar este punto, utilizamos el comando `tshark -nr shark2.pcapng -Y 'frame contains "pico"' -T fields -e text` para ver todas estas banderas "falsas".

```shell()
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{bfe48e8500c454d647c55a4471985e776a07b26cba64526713f43758599aa98b}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{bda69bdf8f570a9aaab0e4108a0fa5f64cb26ba7d2269bb63f68af5d98b98245}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{fe83bcb6cfd43d3b79392f6a4232685f6ed4e7a789c2ce559cf3c1ab6adbe34b}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{711d3893d90f100c15e10ef4842abeed3a830f8237c1257cd47389646da97810}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{3cf1e22d489fcfb6bb312a34f46c8699989ed043406134331452d11ce73cd59e}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{b4cc138bb0f7f9da7e35085e349555aa6d00bdca3b021c1fe8663c0a422ce0d7}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{41b8a1a796bd8d202016f75bc5b38889e9ea06007e6b22fc856d380fb7573133}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{9812bc4be04e6f9c803152313db3da53b3dfb799bdb05aac46fa0dd0045d2fc2}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{64cf3ede3736a340fdf2954be5151ce53bec291c5e48cbccb44faa529946e249}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{c50d259a4e172fcb2eddbabeebd272473e4882b76c9efcd12c03ac04429d884a}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{0a024b7d39603756feafa2bbaa1603b14a99eae5dcd59f1d957f511d822c8c06}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{97211eec9228bb247d762527bace8b3e4ec2110c8834af12aefd3c552cdc21b2}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{29679910c47d8afc737a1c21d7bf758cd3d81001bdbeec8c6f81a6ad88fdc279}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{996979e9540be0fe9320e80eb6336047f8140a80830700907b99741310acf08f}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{8b272a18c1005c95a420d4a0df426cb8441d29eb96210493a96fa25ac5e657aa}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{e1d0a752dc71121200f4bcb1b8cc2e03e84488df229b82196afbe0045ef025c4}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{0ba511844a2ab38fe0709bcdb2b8bdfeb37a0b466dc902e92062db4c2b3f455c}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{dadda48e855421e14597ffc727943b57efd8c9a15d10bfd491f0390659162fb1}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{f4dd87795395c74f3083f8caa4ec22d1531281554a6003d1c47c5f0370984ab6}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{0f30a584680db9e70c7e1c6ca954c2f023b77f3fd2b05bd9aeee6e00dc4da5d7}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{715e4d0d167e862af8825f62d3f4ff8aef20443445a06b1c68572390a2825d29}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{7654ee03f31576e8ed44799fc4fa5ee053d35050000502e878d1fb8022618923}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{068606b5faca0491d97a2b46fdca7f6f81acbd909ce691077fe77e03a3c0939a}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{64ab681ffed33c49b5e8ae0576e22857e9a10ae30cdbee415fb514b84aa58aea}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{8ae3995e726f8f2c3724e2e0522f038aba6649facd378d8965c648233d79a252}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{1c125d267b5811cd25cca2d517e022270aa60f3c8461f4097c685bcca637a6a9}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{824c298d14e1fe369df991af72ab0725d2e7c7d05b9655486873ccc467f4bd6b}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{e1d8dd1b73d5fd7704a16c924ddee69dc6bf9beef14cc3a10142704b81f0fa07}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{82d260fe0670d551347b164c54183d996c52ebeebb1ccfcc2c2ebb91268dc944}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{74876fc61ebc9c902f8983979cd4c21206c69a23f0dcc0817e150dd75e446838}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{49c52d1f30973f90716bbcbe3633e11cf70b9a31ed785871ccb80473302a59db}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{89d93dbb96a3857ac87ba0cea3c10a9e4c7b34d79b2edb463cef030d34297bd0}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{5ceacdce54c13a3fddfcfb225a00247304fbb15f29f9c90434383f277567992d}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{c22a40a43ed7034bd935805f59603a46d3a1f2d6b8e31281eb0721597b6c6d62}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{6071bca5da06d4f975a52357cda0cd6f0614787c1c70b1b7e1af2c7fb272d281}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{65a8b141f019506feea38a119988ad645bcab1a5fa8693efdf26e1fd3cb44b4c}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{d7f5cb78a895d3805601522b95d599cb6d2689c6a856e3fbee6aac2fca0c20f3}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{739bb0f0aa17331819a0e942d37bfee757c8d9cd089cdfe32509027b92485213}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{7a891e2c4ad0da374bc15ad7ad0ee081077dd376f06152781f780c201691713d}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{a97d3ee943221888bd1157429e4a00ed5e9905a610e64664f7e36c7f5e0a4ef9}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{c38d2d74dc21bbb2e3a95b52e2354ee523379cfe4f8b348c9c5b5d7bd7cb871b}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{e4dc886c39a53ff118bf29041067cde48dcebb89b3dae61a8aba6187d671999a}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{9fbd0d18aa1abfd289ba977ae4354b821cc74591260889afba1b0b6e7763aa31}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{3fc0801bcd36336a2c030c6e5f452f5795be1d562e00411365fb64c6a2f688ef}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{4aa86643eb2ddb5709725344cd0e63e6c52e35c2e64a39f3a4a0ee7bbd5d3ade}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{4af8df415d17e6df99a5efddebcb33a68c0c8bf26d481eed16b5f77675030d7f}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{e4f52a0d2a924906ac102a32c52ab9128bf9cd6e5294518ad3ed6748f853b0ab}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{cc104e74a9f50164ee5652d168ef38a21b7a2d5e3196062e669e3a2705f1a0d3}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{2aac620b0bdd2e6946d62c5d232ca32ba1f5a9d8ec82c060778b54ffeb8fbd1f}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{4e55be07159def207afc142954f5673a0651d5f32f5f4090fb774d960628e352}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{983e5e2703a132a49479e438bfba15ee5d02345b03d410b8163b685973937da7}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{d342a46e8179de9941720c5e0eeac0d0fae9d3014d2ddcf531a7865a997b00e5}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{2133904cfe757bc6c68c3e5f3749b37d67d7fa6ffb2768410be593d3fe8c4bd4}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{29b726b9a57d176e1487d159474ee7e6508b66c05c526a00c942a8cebb6bb496}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{7302b0dca07cd890c75e38d78d7e74d7bbf2b932f555aaf5b6754f56e778e3fc}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{22e018bb8282e9d7852ed4e65f70a26524dabef78cf41e1db45c070c94621c57}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{40f366ccf0f6462f5b8b1dc4d7384a62aa95565afcaad96a937b8c1f1134099b}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{db38cbc215cde0d9cd52cbca2390defdb54303e998019a5c4ddaf9861b54efcb}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{090fa8ec995ab9fc9f97cbe9ea36cb81c4504a3ca02466ddd207cfe7f785cb5c}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{947b91a983c93217304f8e5b112e93eaf619e6a9386ab93be93a9b67e53b2fda}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{a3ed2f602322f749f4cb016515e25b67749efd08ac2f2c53023596cbf0dcbd0f}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{8e625859eb325d2a69934e4a44c93fcc132e813efb3fdaaa5143147678e9cbf9}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{8d43c4889ee5b507d1785adfa2592f2fb3d7cf20ebf37ce46595edc46fba3f6d}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{0020d021e9e38dbb5a5fa432175089d8b76e4a900618c95f8cae14fedaa45b63}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{69e96b10f560a6a0656a6d950e73e41bcf4226c424bb5622839dda0c66755b14}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{34c6ca47d858ab18aa2008f4ac31c31570c46186939e6b46458b19082122d4bd}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{ebfcebe696b1fdbba2abb3b003165152456bd83b6ddfbf180ca366de0dec1b0c}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{aa125aaeb4723f69dceaa90125a8099a6f3fe0259e068fd82dcbeb76131448bb}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{80d65857d8d81a92769e8cd136376522d113c4298b331318ce7adcbf5e70104d}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{00ae773ce4a4b3cf3287f072c13ec7139a74207de635de9d115087bc4f312bae}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{7e808778b7250893922a17d53f10365b009a7624935850ac5c8140461e49d579}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{33e80d6e9f56c1f7705c73566d347ccb32b4662171f224b6dfcb6c8fce4f1601}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{5d921ffbe2709ba82d09603a095530aedae41ab96fd052140cbc64319b7ab0ac}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{977b385d5dd6abde9cb89ee940b5cfb7179d73d989c6993346d278bff003c154}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{ca7d3b029817de8f318d8fa521ad1b569f4e8a37358373193522cc7f5628ed49}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{a820680ab6444b1daf5281192f337aefb4aa95a313c9f270804ef7826ecc298c}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{998d01dadf1b44eb4ec7b7e8fa11f11bcd2d7d86f3f9e4966dde22d4a84ca113}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{cb8fe3ec65f890e2f0570c98c4edd3fe4115bc059ac2afb39300c7b66f2302c4}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{bc2af8cbe0ae0befdd28b14412295243354cd3c7cc74e88d8facb2fd5e6ef34d}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{09082a0313e16fc36f8076ff86e54e83048a8568f5c2294fea5fb3bcd212e7f2}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{2386746aeb258914349dc81a85cb5de72e47930c7f11759b4ad9f864efa7b5aa}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{173306d7b886423d9f79d3d0d05209807ae7b83c445931319830e4e0ad2d2f09}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{6cb98e2295bbe1f15fd8b8b5908de360d386b98a0ce7e0407e001b453b05be22}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{132e643c8fdadb54c366072cb33940411fcfd355209fc1ce9b2022ad1cd1b060}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{044ffca72f0f191b0715ff1a9bff182c810cb2786370cbf8cdc1943c2e7aedf6}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{b278104c2602442e3db401749c30527d80ba560f9a02c939cb4ff6ea189a140d}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{7282e048d6d32383b65f3a03b1101219ac73f7f538446b78d1b2b334e0985447}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{98406c4acbf0f57b3ccbc923aab5a603d70f86d507f422d9bd8656398f53433e}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{3fe0b2788f30d9cb9f77d3b2752f13c554fe7f0e7a2883e57c8a44b34f35675c}
```

- Despues de esto, yo procedia analizar los paquetes DNS, ya que tambien habia muchos, para lo que filtre solo sols archivos dns poniendo en la barra de busqueda `dns`.
- Al estar analizando estos datos, vemos que hay un grupo muy pequeño de ip's de destino; `18.217.1.57`.
- por lo que poniendo en la barra de busqueda, filtraremos estos paquetes con `dns and ip.dst==18.217.1.57dns and ip.dst==18.217.1.57`.
- Podemos notar que si vamos a los dominios y los ordenamos podemos encontrar fragmentos de una cadena codificada en base 64:

```bash()
cGljb0NURntkbnNfM3hmMWxfZnR3X2RlYWRiZWVmfQ==
```

Si la decodificamos, podemos obtener que la flag es:

```bash()
picoCTF{dns_3xf1l_ftw_deadbeef} 
```

## Notas adicionales
- La línea de comando `tshark -nr shark2.pcapng -Y 'frame contains "pico"' -T fields -e text` es una herramienta de análisis de red que utiliza el programa Wireshark. Esta línea de comando filtra los paquetes capturados en el archivo `shark2.pcapng` para mostrar sólo aquellos que contienen la cadena de texto "pico". La opción `-T fields` especifica que se deben mostrar sólo ciertos campos del paquete, y la opción `-e text` indica que se debe mostrar el campo "text". Esto dará como resultado una lista de todos los paquetes que contienen la cadena de texto "pico" y el contenido del campo "text" para cada uno de estos paquetes.
- La opción `-nr` en el comando `tshark` indica que el archivo de entrada para el análisis de red es un archivo de captura de paquetes en formato pcap o pcapng. En este caso, el archivo de entrada es `shark2.pcapng`.

## Referencias 
- [Script de apoyo 1](https://picoctf2021.haydenhousen.com/forensics/wireshark-twoo-twooo-two-twoo...)
- [Script de apoyo 2](https://github.com/Dvd848/CTFs/blob/master/2021_picoCTF/Wireshark_twoo_twooo_two_twoo.md)
- 
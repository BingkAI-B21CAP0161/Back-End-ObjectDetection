<!doctype html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="Mark Otto, Jacob Thornton, and Bootstrap contributors">
    <meta name="generator" content="Hugo 0.83.1">
    <title>Signin Template · Bootstrap v5.0</title>

    <link rel="canonical" href="https://getbootstrap.com/docs/5.0/examples/sign-in/">



    <!-- Bootstrap core CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-+0n0xVW2eSR5OomGNYDnhzAbDsOXxcvSN1TPprVMTNDbiYZCxYbOOl7+AMvyTG2x" crossorigin="anonymous">



    <style>
        .bd-placeholder-img {
            font-size: 1.125rem;
            text-anchor: middle;
            -webkit-user-select: none;
            -moz-user-select: none;
            user-select: none;
        }

        @media (min-width: 768px) {
            .bd-placeholder-img-lg {
                font-size: 3.5rem;
            }
        }
    </style>
</head>

<body class="text-center container pt-5">
    <div class="card">
        <div class="card-body">
            <main class="form-signin">
                <form action="<?= base_url('home/klasifikasi')?>" enctype="multipart/form-data" method="POST">
                    <div class="input-group mb-3">
                        <label class="input-group">Unggah Foto</label>
                        <input type="file" name="photo" class="form-control">
                    </div>
                    <div class="input-group mb-3">
                        <label class="input-group">Keterangan</label>
                        <input type="text" name="keterangan" class="form-control">
                    </div>
                    <button type="submit" class="btn btn-success">Unggah</button>
                </form>
            </main>
        </div>
    </div>



</body>

</html>
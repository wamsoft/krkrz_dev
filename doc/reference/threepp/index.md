# krkrthreepp (threepp 3D) リファレンス

threepp (three.js 互換 C++ 3D エンジン) を吉里吉里Zから扱うプラグイン `krkrthreepp` が提供するクラス群のリファレンスです。
3D シーン構築・ジオメトリ・マテリアル・カメラ・ライト・カーブ/シェイプ・アニメーション・VRM/glTF ローダなど計 110 クラスを収録しています。

プラグイン概要・使用例は `src/plugins/krkrthreepp/README.md` を参照してください。

- [Threepp (名前空間)](Threepp.md) — threepp プラグイン 擬似コードによるマニュアル

## クラス一覧

| クラス | 概要 |
|---|---|
| [AmbientLight](Threepp.AmbientLight.md) | 環境光 |
| [AnimationAction](Threepp.AnimationAction.md) | 再生中の1アニメーション (ModelAnimator.clipAction/play が返す) |
| [ArrowHelper](Threepp.ArrowHelper.md) | 矢印ヘルパー |
| [AxesHelper](Threepp.AxesHelper.md) | 軸ヘルパー |
| [Bone](Threepp.Bone.md) | ボーン |
| [Box2](Threepp.Box2.md) | 2D 軸平行境界ボックスクラス |
| [Box3](Threepp.Box3.md) | 軸平行境界ボックス (AABB) クラス |
| [BoxGeometry](Threepp.BoxGeometry.md) | ボックス（立方体）ジオメトリ |
| [BoxHelper](Threepp.BoxHelper.md) | ボックスヘルパー |
| [BufferGeometry](Threepp.BufferGeometry.md) | バッファジオメトリ基底クラス |
| [Camera](Threepp.Camera.md) | カメラ基底クラス |
| [CameraHelper](Threepp.CameraHelper.md) | カメラヘルパー |
| [CapsuleGeometry](Threepp.CapsuleGeometry.md) | カプセルジオメトリ |
| [CatmullRomCurve3](Threepp.CatmullRomCurve3.md) | CatmullRom スプライン曲線 |
| [CircleGeometry](Threepp.CircleGeometry.md) | 円（ディスク）ジオメトリ |
| [Clock](Threepp.Clock.md) | タイマークラス |
| [Color](Threepp.Color.md) | 色クラス |
| [ConeGeometry](Threepp.ConeGeometry.md) | 円錐ジオメトリ |
| [CubicBezierCurve](Threepp.CubicBezierCurve.md) | 2D三次ベジェカーブ |
| [CubicBezierCurve3](Threepp.CubicBezierCurve3.md) | 3D三次ベジェカーブ |
| [CylinderGeometry](Threepp.CylinderGeometry.md) | 円柱ジオメトリ |
| [Cylindrical](Threepp.Cylindrical.md) | 円柱座標クラス |
| [DataTexture](Threepp.DataTexture.md) | データテクスチャ |
| [DirectionalLight](Threepp.DirectionalLight.md) | 平行光源（太陽光のような光） |
| [DirectionalLightHelper](Threepp.DirectionalLightHelper.md) | ディレクショナルライトヘルパー |
| [EdgesGeometry](Threepp.EdgesGeometry.md) | エッジジオメトリ |
| [EllipseCurve](Threepp.EllipseCurve.md) | 楕円カーブ |
| [Euler](Threepp.Euler.md) | オイラー角クラス |
| [ExtrudeGeometry](Threepp.ExtrudeGeometry.md) | ExtrudeGeometry（押し出しジオメトリ） |
| [Fog](Threepp.Fog.md) | フォグ（線形） |
| [FogExp2](Threepp.FogExp2.md) | フォグ（指数関数） |
| [GLRenderer](Threepp.GLRenderer.md) | OpenGL レンダラー |
| [GLTFLoader](Threepp.GLTFLoader.md) | 汎用 glTF/GLB ローダ |
| [GLTFModel](Threepp.GLTFModel.md) | ロード済み glTF モデル (GLTFLoader の戻り値) |
| [GridHelper](Threepp.GridHelper.md) | グリッドヘルパー |
| [Group](Threepp.Group.md) | グループクラス |
| [HemisphereLight](Threepp.HemisphereLight.md) | 半球ライト |
| [IcosahedronGeometry](Threepp.IcosahedronGeometry.md) | 正二十面体ジオメトリ |
| [InstancedMesh](Threepp.InstancedMesh.md) | インスタンスメッシュ |
| [LatheGeometry](Threepp.LatheGeometry.md) | 旋盤ジオメトリ |
| [Light](Threepp.Light.md) | ライト基底クラス |
| [Line](Threepp.Line.md) | 線オブジェクト |
| [Line3](Threepp.Line3.md) | 3D 線分クラス |
| [LineBasicMaterial](Threepp.LineBasicMaterial.md) | 線用基本マテリアル |
| [LineCurve](Threepp.LineCurve.md) | 2D直線カーブ |
| [LineCurve3](Threepp.LineCurve3.md) | 3D直線カーブ |
| [LineSegments](Threepp.LineSegments.md) | 線分オブジェクト |
| [LOD](Threepp.LOD.md) | LOD (Level of Detail) |
| [Material](Threepp.Material.md) | マテリアル基底クラス |
| [Matrix3](Threepp.Matrix3.md) | 3x3 行列クラス |
| [Matrix4](Threepp.Matrix4.md) | 4x4 行列クラス |
| [Mesh](Threepp.Mesh.md) | メッシュクラス |
| [MeshBasicMaterial](Threepp.MeshBasicMaterial.md) | 基本マテリアル |
| [MeshDepthMaterial](Threepp.MeshDepthMaterial.md) | 深度マテリアル |
| [MeshLambertMaterial](Threepp.MeshLambertMaterial.md) | Lambert マテリアル |
| [MeshMatcapMaterial](Threepp.MeshMatcapMaterial.md) | マットキャップマテリアル |
| [MeshNormalMaterial](Threepp.MeshNormalMaterial.md) | 法線マテリアル |
| [MeshPhongMaterial](Threepp.MeshPhongMaterial.md) | Phong マテリアル |
| [MeshStandardMaterial](Threepp.MeshStandardMaterial.md) | Standard PBR マテリアル |
| [MeshToonMaterial](Threepp.MeshToonMaterial.md) | トゥーン（セルシェーディング）マテリアル |
| [ModelAnimator](Threepp.ModelAnimator.md) | モデルアニメーション再生機 (three.js の AnimationMixer 相当) |
| [Object3D](Threepp.Object3D.md) | 3Dオブジェクトの基底クラス |
| [OctahedronGeometry](Threepp.OctahedronGeometry.md) | 正八面体ジオメトリ |
| [OrthographicCamera](Threepp.OrthographicCamera.md) | 正射影カメラ |
| [Path](Threepp.Path.md) | 2Dパス |
| [PerspectiveCamera](Threepp.PerspectiveCamera.md) | 透視投影カメラ |
| [Plane](Threepp.Plane.md) | 平面クラス |
| [PlaneGeometry](Threepp.PlaneGeometry.md) | 平面ジオメトリ |
| [PlaneHelper](Threepp.PlaneHelper.md) | 平面ヘルパー |
| [PointLight](Threepp.PointLight.md) | 点光源 |
| [PointLightHelper](Threepp.PointLightHelper.md) | ポイントライトヘルパー |
| [Points](Threepp.Points.md) | 点群オブジェクト |
| [PointsMaterial](Threepp.PointsMaterial.md) | 点群用マテリアル |
| [PolarGridHelper](Threepp.PolarGridHelper.md) | 極座標グリッドヘルパー |
| [QuadraticBezierCurve](Threepp.QuadraticBezierCurve.md) | 2D二次ベジェカーブ |
| [QuadraticBezierCurve3](Threepp.QuadraticBezierCurve3.md) | 3D二次ベジェカーブ |
| [Quaternion](Threepp.Quaternion.md) | クォータニオン（四元数）クラス |
| [RawShaderMaterial](Threepp.RawShaderMaterial.md) | Raw シェーダーマテリアル |
| [Ray](Threepp.Ray.md) | 光線クラス |
| [Raycaster](Threepp.Raycaster.md) | レイキャスター |
| [Reflector](Threepp.Reflector.md) | 反射面オブジェクト |
| [RingGeometry](Threepp.RingGeometry.md) | リング（環状）ジオメトリ |
| [Scene](Threepp.Scene.md) | シーンクラス |
| [ShaderMaterial](Threepp.ShaderMaterial.md) | シェーダーマテリアル |
| [Shape](Threepp.Shape.md) | Shape（穴付き2D形状） |
| [ShapeGeometry](Threepp.ShapeGeometry.md) | ShapeGeometry（2D形状ジオメトリ） |
| [Skeleton](Threepp.Skeleton.md) | スケルトン |
| [SkinnedMesh](Threepp.SkinnedMesh.md) | スキニングメッシュ |
| [Sky](Threepp.Sky.md) | 空オブジェクト |
| [Sphere](Threepp.Sphere.md) | 球クラス |
| [SphereGeometry](Threepp.SphereGeometry.md) | 球ジオメトリ |
| [Spherical](Threepp.Spherical.md) | 球面座標クラス |
| [SplineCurve](Threepp.SplineCurve.md) | 2Dスプラインカーブ |
| [SpotLight](Threepp.SpotLight.md) | スポットライト |
| [SpotLightHelper](Threepp.SpotLightHelper.md) | スポットライトヘルパー |
| [Sprite](Threepp.Sprite.md) | スプライトオブジェクト |
| [SpriteMaterial](Threepp.SpriteMaterial.md) | スプライト用マテリアル |
| [Texture](Threepp.Texture.md) | テクスチャ基底クラス |
| [TextureLoader](Threepp.TextureLoader.md) | テクスチャローダー |
| [TorusGeometry](Threepp.TorusGeometry.md) | トーラス（ドーナツ形状）ジオメトリ |
| [TorusKnotGeometry](Threepp.TorusKnotGeometry.md) | トーラスノットジオメトリ |
| [Triangle](Threepp.Triangle.md) | 三角形クラス |
| [Vector2](Threepp.Vector2.md) | 2D ベクトルクラス |
| [Vector3](Threepp.Vector3.md) | 3D ベクトルクラス |
| [VRM](Threepp.VRM.md) | VRM モデル 1 体 |
| [VRMAnimation](Threepp.VRMAnimation.md) | VRM アニメーション (.vrma / VRMC_vrm_animation) |
| [VRMAnimationLoader](Threepp.VRMAnimationLoader.md) | VRM アニメーションローダ |
| [VRMLoader](Threepp.VRMLoader.md) | VRM ローダ |
| [Water](Threepp.Water.md) | 水面オブジェクト |
| [WireframeGeometry](Threepp.WireframeGeometry.md) | ワイヤーフレームジオメトリ |

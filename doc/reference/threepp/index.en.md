---
source_hash: 14703ef61738
---

# krkrthreepp (threepp 3D) Reference

Reference for the classes provided by the `krkrthreepp` plugin, which makes threepp (a three.js-compatible C++ 3D engine) available from Kirikiri Z.
It covers 110 classes in total, including 3D scene construction, geometries, materials, cameras, lights, curves/shapes, animation, and VRM/glTF loaders.

For a plugin overview and usage examples, see `src/plugins/krkrthreepp/README.md`.

- [Threepp (namespace)](Threepp.md) — threepp plugin manual written as pseudo-code

## Class list

| Class | Summary |
|---|---|
| [AmbientLight](Threepp.AmbientLight.md) | Ambient light |
| [AnimationAction](Threepp.AnimationAction.md) | A single playing animation (returned by ModelAnimator.clipAction/play) |
| [ArrowHelper](Threepp.ArrowHelper.md) | Arrow helper |
| [AxesHelper](Threepp.AxesHelper.md) | Axes helper |
| [Bone](Threepp.Bone.md) | Bone |
| [Box2](Threepp.Box2.md) | 2D axis-aligned bounding box class |
| [Box3](Threepp.Box3.md) | Axis-aligned bounding box (AABB) class |
| [BoxGeometry](Threepp.BoxGeometry.md) | Box (cuboid) geometry |
| [BoxHelper](Threepp.BoxHelper.md) | Box helper |
| [BufferGeometry](Threepp.BufferGeometry.md) | Buffer geometry base class |
| [Camera](Threepp.Camera.md) | Camera base class |
| [CameraHelper](Threepp.CameraHelper.md) | Camera helper |
| [CapsuleGeometry](Threepp.CapsuleGeometry.md) | Capsule geometry |
| [CatmullRomCurve3](Threepp.CatmullRomCurve3.md) | Catmull-Rom spline curve |
| [CircleGeometry](Threepp.CircleGeometry.md) | Circle (disc) geometry |
| [Clock](Threepp.Clock.md) | Timer class |
| [Color](Threepp.Color.md) | Color class |
| [ConeGeometry](Threepp.ConeGeometry.md) | Cone geometry |
| [CubicBezierCurve](Threepp.CubicBezierCurve.md) | 2D cubic Bezier curve |
| [CubicBezierCurve3](Threepp.CubicBezierCurve3.md) | 3D cubic Bezier curve |
| [CylinderGeometry](Threepp.CylinderGeometry.md) | Cylinder geometry |
| [Cylindrical](Threepp.Cylindrical.md) | Cylindrical coordinates class |
| [DataTexture](Threepp.DataTexture.md) | Data texture |
| [DirectionalLight](Threepp.DirectionalLight.md) | Directional light (like sunlight) |
| [DirectionalLightHelper](Threepp.DirectionalLightHelper.md) | Directional light helper |
| [EdgesGeometry](Threepp.EdgesGeometry.md) | Edges geometry |
| [EllipseCurve](Threepp.EllipseCurve.md) | Ellipse curve |
| [Euler](Threepp.Euler.md) | Euler angles class |
| [ExtrudeGeometry](Threepp.ExtrudeGeometry.md) | ExtrudeGeometry (extruded geometry) |
| [Fog](Threepp.Fog.md) | Fog (linear) |
| [FogExp2](Threepp.FogExp2.md) | Fog (exponential) |
| [GLRenderer](Threepp.GLRenderer.md) | OpenGL renderer |
| [GLTFLoader](Threepp.GLTFLoader.md) | General-purpose glTF/GLB loader |
| [GLTFModel](Threepp.GLTFModel.md) | Loaded glTF model (return value of GLTFLoader) |
| [GridHelper](Threepp.GridHelper.md) | Grid helper |
| [Group](Threepp.Group.md) | Group class |
| [HemisphereLight](Threepp.HemisphereLight.md) | Hemisphere light |
| [IcosahedronGeometry](Threepp.IcosahedronGeometry.md) | Icosahedron geometry |
| [InstancedMesh](Threepp.InstancedMesh.md) | Instanced mesh |
| [LatheGeometry](Threepp.LatheGeometry.md) | Lathe geometry |
| [Light](Threepp.Light.md) | Light base class |
| [Line](Threepp.Line.md) | Line object |
| [Line3](Threepp.Line3.md) | 3D line segment class |
| [LineBasicMaterial](Threepp.LineBasicMaterial.md) | Basic material for lines |
| [LineCurve](Threepp.LineCurve.md) | 2D line curve |
| [LineCurve3](Threepp.LineCurve3.md) | 3D line curve |
| [LineSegments](Threepp.LineSegments.md) | Line segments object |
| [LOD](Threepp.LOD.md) | LOD (Level of Detail) |
| [Material](Threepp.Material.md) | Material base class |
| [Matrix3](Threepp.Matrix3.md) | 3x3 matrix class |
| [Matrix4](Threepp.Matrix4.md) | 4x4 matrix class |
| [Mesh](Threepp.Mesh.md) | Mesh class |
| [MeshBasicMaterial](Threepp.MeshBasicMaterial.md) | Basic material |
| [MeshDepthMaterial](Threepp.MeshDepthMaterial.md) | Depth material |
| [MeshLambertMaterial](Threepp.MeshLambertMaterial.md) | Lambert material |
| [MeshMatcapMaterial](Threepp.MeshMatcapMaterial.md) | Matcap material |
| [MeshNormalMaterial](Threepp.MeshNormalMaterial.md) | Normal material |
| [MeshPhongMaterial](Threepp.MeshPhongMaterial.md) | Phong material |
| [MeshStandardMaterial](Threepp.MeshStandardMaterial.md) | Standard PBR material |
| [MeshToonMaterial](Threepp.MeshToonMaterial.md) | Toon (cel-shading) material |
| [ModelAnimator](Threepp.ModelAnimator.md) | Model animation player (equivalent to three.js AnimationMixer) |
| [Object3D](Threepp.Object3D.md) | Base class for 3D objects |
| [OctahedronGeometry](Threepp.OctahedronGeometry.md) | Octahedron geometry |
| [OrthographicCamera](Threepp.OrthographicCamera.md) | Orthographic camera |
| [Path](Threepp.Path.md) | 2D path |
| [PerspectiveCamera](Threepp.PerspectiveCamera.md) | Perspective camera |
| [Plane](Threepp.Plane.md) | Plane class |
| [PlaneGeometry](Threepp.PlaneGeometry.md) | Plane geometry |
| [PlaneHelper](Threepp.PlaneHelper.md) | Plane helper |
| [PointLight](Threepp.PointLight.md) | Point light |
| [PointLightHelper](Threepp.PointLightHelper.md) | Point light helper |
| [Points](Threepp.Points.md) | Point cloud object |
| [PointsMaterial](Threepp.PointsMaterial.md) | Material for point clouds |
| [PolarGridHelper](Threepp.PolarGridHelper.md) | Polar grid helper |
| [QuadraticBezierCurve](Threepp.QuadraticBezierCurve.md) | 2D quadratic Bezier curve |
| [QuadraticBezierCurve3](Threepp.QuadraticBezierCurve3.md) | 3D quadratic Bezier curve |
| [Quaternion](Threepp.Quaternion.md) | Quaternion class |
| [RawShaderMaterial](Threepp.RawShaderMaterial.md) | Raw shader material |
| [Ray](Threepp.Ray.md) | Ray class |
| [Raycaster](Threepp.Raycaster.md) | Raycaster |
| [Reflector](Threepp.Reflector.md) | Reflective surface object |
| [RingGeometry](Threepp.RingGeometry.md) | Ring (annulus) geometry |
| [Scene](Threepp.Scene.md) | Scene class |
| [ShaderMaterial](Threepp.ShaderMaterial.md) | Shader material |
| [Shape](Threepp.Shape.md) | Shape (2D shape with holes) |
| [ShapeGeometry](Threepp.ShapeGeometry.md) | ShapeGeometry (2D shape geometry) |
| [Skeleton](Threepp.Skeleton.md) | Skeleton |
| [SkinnedMesh](Threepp.SkinnedMesh.md) | Skinned mesh |
| [Sky](Threepp.Sky.md) | Sky object |
| [Sphere](Threepp.Sphere.md) | Sphere class |
| [SphereGeometry](Threepp.SphereGeometry.md) | Sphere geometry |
| [Spherical](Threepp.Spherical.md) | Spherical coordinates class |
| [SplineCurve](Threepp.SplineCurve.md) | 2D spline curve |
| [SpotLight](Threepp.SpotLight.md) | Spotlight |
| [SpotLightHelper](Threepp.SpotLightHelper.md) | Spotlight helper |
| [Sprite](Threepp.Sprite.md) | Sprite object |
| [SpriteMaterial](Threepp.SpriteMaterial.md) | Material for sprites |
| [Texture](Threepp.Texture.md) | Texture base class |
| [TextureLoader](Threepp.TextureLoader.md) | Texture loader |
| [TorusGeometry](Threepp.TorusGeometry.md) | Torus (donut-shaped) geometry |
| [TorusKnotGeometry](Threepp.TorusKnotGeometry.md) | Torus knot geometry |
| [Triangle](Threepp.Triangle.md) | Triangle class |
| [Vector2](Threepp.Vector2.md) | 2D vector class |
| [Vector3](Threepp.Vector3.md) | 3D vector class |
| [VRM](Threepp.VRM.md) | A single VRM model |
| [VRMAnimation](Threepp.VRMAnimation.md) | VRM animation (.vrma / VRMC_vrm_animation) |
| [VRMAnimationLoader](Threepp.VRMAnimationLoader.md) | VRM animation loader |
| [VRMLoader](Threepp.VRMLoader.md) | VRM loader |
| [Water](Threepp.Water.md) | Water surface object |
| [WireframeGeometry](Threepp.WireframeGeometry.md) | Wireframe geometry |

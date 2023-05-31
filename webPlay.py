import uvicorn
from vidgear.gears.asyncio import WebGear

options = {
    "frame_size_reduction": 40, # frame尺寸减少40%
    "jpeg_compression_quality": 80, # jpeg图质量
    "jpeg_compression_fastdct": False, # 使用fastdct快速编码
    "jpeg_compression_fastupsample": False,
}

web = WebGear(source="test.mp4", logging=True, **options)
uvicorn.run(web(), host="localhost", port = 8088)